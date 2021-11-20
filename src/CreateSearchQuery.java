import com.mongodb.*;
import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoDatabase;
import org.bson.Document;

public class CreateSearchQuery {

    private static class SearchQuery {
        String tickerSymbol;
        char timeFrame = 'h';
        boolean showNews = false;

        private boolean timeFrameInvalid(char input) {
            return !switch (input) {
                case 'm', 'd', 'M', 'y', 'a', 'h' -> true;
                default -> false;
            };
        }

        private SearchQuery(String tickerSymbol) {
            this.tickerSymbol = tickerSymbol;
        }

        private SearchQuery(String tickerSymbol, char timeFrame) {
            this.tickerSymbol = tickerSymbol;
            if (timeFrameInvalid(timeFrame)) {
                throw new IllegalArgumentException("Invalid Time Frame value: " + timeFrame + "\nValid values are: 'm' (minutes), 'h' (hours), 'd' (days), 'M' (months), 'y' (years), 'a' (all))");
            }
            this.timeFrame = timeFrame;
        }

        private SearchQuery(String tickerSymbol, char timeFrame, boolean showNews) {
            this.tickerSymbol = tickerSymbol;
            this.showNews = showNews;
            if (timeFrameInvalid(timeFrame)) {
                throw new IllegalArgumentException("Invalid Time Frame value: " + timeFrame + "\nValid values are: 'm' (minutes), 'h' (hours), 'd' (days), 'M' (months), 'y' (years), 'a' (all))");
            }
            this.timeFrame = timeFrame;
        }

        private Document createQuery() {
            return new Document()
                    .append("tickerSymbol", tickerSymbol)
                    .append("timeFrame", timeFrame)
                    .append("showNews", showNews);
        }
    }


    private static MongoClient client() {
        return new MongoClient(new MongoClientURI("mongodb+srv://finn:sauber@cluster0.4gtm6.mongodb.net/test"));
    }

    private static MongoCollection<Document> getQueryCollection(MongoDatabase db) {
        return db.getCollection("Waitlist");
    }


    public static void main(String[] args) {
        MongoClient mainClient = client();

        MongoDatabase mainClientDatabase = mainClient.getDatabase("Algo");
        MongoCollection<Document> collection = getQueryCollection(mainClientDatabase);

        SearchQuery query = new SearchQuery("AAPL");
        collection.insertOne(query.createQuery());
    }
}
