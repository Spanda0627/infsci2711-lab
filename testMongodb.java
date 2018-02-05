/**
 * Created by fan on 2/4/18.
 */

import com.mongodb.*;

import java.util.List;
import java.util.Set;

public class testMongodb {

    public static void main(String[] args) {

        try {

            /* Connect to Cluster */
            MongoClientURI uri = new MongoClientURI(
                    "mongodb+srv://yfamy123:<password>@cluster0-fnmen.mongodb.net/test");
            MongoClient mongoClient = new MongoClient(uri);

            /* Connect to Local */
//            MongoClient mongoClient = new MongoClient();

            System.out.println("Connect successfully!");

            List<String> databaseNames = mongoClient.getDatabaseNames();

            System.out.println("Database list");
            for(String db : databaseNames) {
                System.out.println(db);
            }

            DB database = mongoClient.getDB("test");

            Set<String> collectionNames = database.getCollectionNames();

            System.out.println("Collection list in database test");
            for(String collection : collectionNames) {
                System.out.println(collection);
            }

            DBCollection restaurant = database.getCollection("restaurants");

            System.out.println("Show one document in the collection");
            System.out.println(restaurant.findOne());

            BasicDBObject whereQuery = new BasicDBObject();
            whereQuery.put("name", "Wendy'S");

            DBCursor cursor = restaurant.find(whereQuery);
            while(cursor.hasNext()) {
                System.out.println(cursor.next());
            }


        } catch (Exception e) {
            System.out.println("Could not connect to MongoDB");
        }

    }



}
