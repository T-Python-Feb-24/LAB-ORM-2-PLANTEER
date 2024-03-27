BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "auth_user" (
	"id"	integer NOT NULL,
	"password"	varchar(128) NOT NULL,
	"last_login"	datetime,
	"is_superuser"	bool NOT NULL,
	"username"	varchar(150) NOT NULL UNIQUE,
	"first_name"	varchar(150) NOT NULL,
	"last_name"	varchar(150) NOT NULL,
	"is_staff"	bool NOT NULL,
	"is_active"	bool NOT NULL,
	"date_joined"	datetime NOT NULL,
	"email"	varchar(254) NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "main_contact" (
	"id"	integer NOT NULL,
	"first_name"	varchar(20) NOT NULL,
	"last_name"	varchar(20) NOT NULL,
	"email"	varchar(254) NOT NULL,
	"message"	text NOT NULL,
	"created_at"	datetime NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "main_plant" (
	"id"	integer NOT NULL,
	"name"	varchar(20) NOT NULL,
	"about"	text NOT NULL,
	"used_for"	text NOT NULL,
	"image"	varchar(100) NOT NULL,
	"category"	varchar(10) NOT NULL,
	"is_edible"	bool NOT NULL,
	"created_at"	datetime NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "main_comment" (
	"id"	integer NOT NULL,
	"content"	text NOT NULL,
	"comment_date"	datetime NOT NULL,
	"user_id"	integer NOT NULL,
	"plant_id"	bigint NOT NULL,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("plant_id") REFERENCES "main_plant"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
INSERT INTO "auth_user" ("id","password","last_login","is_superuser","username","first_name","last_name","is_staff","is_active","date_joined","email") VALUES (1,'pbkdf2_sha256$720000$HuUDnZ5pOrVYf17El8J66M$2Rt2u7nlgbhRs7wcqO65SDUJ1wjqmkVaUCkPBSkKTC0=','2024-03-26 07:51:25.116706',1,'admin','','',1,1,'2024-03-25 09:57:49.140617','admin@localhost.dev'),
 (2,'pbkdf2_sha256$720000$YRgZw6aN5XIY1npe84z67B$PDWGDE1DQSST9cMfi+KspfcrqrtvUvHExAQ8gi08Aks=','2024-03-25 12:52:08.333569',0,'ahmed','ahmed','mohmmed',0,1,'2024-03-25 09:51:52.050584','ahmed@gmail.com'),
 (3,'pbkdf2_sha256$720000$1OJ2ugETT1xosU98zmOrZ6$TLJcYyx8SxSRMu628k5yFiNlmNE5zSjQGAspnH9/M1I=','2024-03-26 09:46:26.519845',0,'wissam','wissam','zaidi',0,1,'2024-03-25 13:26:21.291678','admin@admin.sa'),
 (4,'pbkdf2_sha256$720000$iSTxEu0QMzAOajMzH7w0LD$NoIi395a08sD67Dd9vL++4frDVyz6uFFQXTTGOJZF8A=',NULL,0,'aas','assa','ddss',0,1,'2024-03-26 07:54:23.073098','ahmad@gmail.com');
INSERT INTO "main_contact" ("id","first_name","last_name","email","message","created_at") VALUES (1,'ahmad','Gamdi','ahmad@gmail.com','good job','2024-03-23 12:53:08.673606'),
 (2,'Ahmed ','Mohammed','moh@gmail.com','Body text for whatever you''d like to suggest. Add
main takeaway points, quotes, anecdotes, or even a
very very Short Story.','2024-03-23 22:53:43.318825'),
 (3,'Ahmed','Mohammed','ahmad@gmail.com','Lorem ipsum dolor sit amet consectetur adipisicing elit. Praesentium quia, officiis earum consectetur suscipit cumque, illo magni commodi atque aliquid ullam nemo sunt voluptate sapiente at amet impedit! Iste, dolorum.
Asperiores rerum sunt consequuntur, aut ea voluptas quidem veniam est, reprehenderit maxime harum hic laborum itaque magnam nisi, quod voluptates! Obcaecati, odit velit necessitatibus cum animi libero quis possimus deleniti.
Blanditiis consequuntur eum, perspiciatis id laudantium eos magni molestias repellendus quibusdam cum necessitatibus quis? Inventore voluptatum illo alias doloribus maxime dignissimos, ex repellat! Explicabo, dignissimos distinctio illo unde repellendus deleniti.
Exercitationem soluta ut tempora fugit aut temporibus sed aspernatur corporis expedita? Doloremque repellat sed magnam voluptas dolorem ea explicabo enim illo impedit! Corrupti doloribus aliquid fugit totam assumenda, possimus repudiandae.','2024-03-23 22:58:13.365708');
INSERT INTO "main_plant" ("id","name","about","used_for","image","category","is_edible","created_at") VALUES (1,'Apple','An apple is a round, edible fruit produced by an apple tree (Malus spp., among them the domestic or orchard apple; Malus domestica). Apple trees are cultivated worldwide and are the most widely grown species in the genus Malus. The tree originated in Central Asia, where its wild ancestor, Malus sieversii, is still found. Apples have been grown for thousands of years in Asia and Europe and were introduced to North America by European colonists. Apples have religious and mythological significance in many cultures, including Norse, Greek, and European Christian tradition.','lower your chance of developing cancer, diabetes, and heart disease. Research says apples may also help you lose weight while improving your gut and brain','images/plants/fruit_apple.png','Fruit',1,'2024-03-21 07:36:33.995809'),
 (2,'Orange','An orange, also called sweet orange to distinguish it from the bitter orange Citrus × aurantium, is the fruit of a tree in the family Rutaceae. Botanically, this is the hybrid Citrus × sinensis, between the pomelo (Citrus maxima) and the mandarin orange (Citrus reticulata). The chloroplast genome, and therefore the maternal line, is that of pomelo. The sweet orange has had its full genome sequenced.','The vitamin C found in oranges has other health benefits too: Forms blood vessels, muscles, cartilage, and collagen in your bones. Fights inflammation and can reduce the severity of conditions like asthma, rheumatoid arthritis, and cancer. Boosts the body''s immune system to protect against viruses and germs.','images/plants/fruit_orange.png','Fruit',1,'2024-03-21 07:38:09.319644'),
 (3,'Nerium oleander','most commonly known as oleander or nerium, is a shrub or small tree cultivated worldwide in temperate and subtropical areas as an ornamental and landscaping plant. It is the only species currently classified in the genus Nerium, belonging to subfamily Apocynoideae of the dogbane family Apocynaceae. It is so widely cultivated that no precise region of origin has been identified, though it is usually associated with the Mediterranean Basin.

As beautiful as its flowers look, the oleander is highly poisonous. Let us show you how to recognise and treat oleander poisoning in humans and animals. Oleander (Nerium oleander) should be grown with extreme caution. All parts of the plant contain substances toxic to humans.','Its ethnomedicinal uses include treatment of diverse ailments such as heart failure, asthma, corns, cancer, diabetes, and epilepsy. Less well appreciated are the skin care benefits of extracts of N. oleander that include antibacterial, antiviral, immune, and even antitumor properties associated with topical use.','images/plants/flower-nun_Oleander.png','Flawer',0,'2024-03-21 07:41:45.295163'),
 (4,'Maclura pomifera','Maclura pomifera, commonly known as the Osage orange , is a small deciduous tree or large shrub, native to the south-central United States. It typically grows about 8 to 15 metres (30–50 ft) tall. The distinctive fruit, a multiple fruit, is roughly spherical, bumpy, 8 to 15 centimetres (3–6 in) in diameter, and turns bright yellow-green in the fall.[5] The fruits secrete a sticky white latex when cut or damaged. Despite the name "Osage orange", it is not related to the orange. It is a member of the mulberry family, Moraceae','At present, florists use the fruits of M. pomifera for decorative purposes. When dried, the wood has the highest heating value of any commonly available North American wood, and burns long and hot. Osage orange wood is more rot-resistant than most, making good fence posts.','images/plants/fruit-nun_Maclura_Pomifera.jpg','Fruit',0,'2024-03-21 07:44:39.388291'),
 (5,'Agaricus bisporus','Agaricus bisporus, commonly known as the cultivated mushroom, is a basidiomycete mushroom native to grasslands in Eurasia and North America. It is cultivated in more than 70 countries and is one of the most commonly and widely consumed mushrooms in the world. It has two color states while immature – white and brown – both of which have various names, with additional names for the mature state, such as chestnut, portobello, portabellini, button and champignon de Paris.','used in a wide range of recipes and cooking techniques, from tarts and omelets to pasta, risotto, and pizza. They''re the workhorse of the mushroom family, and their mild flavor and meaty texture make them extremely versatile.','images/plants/mushroom_Button-Mushroom.jpg','Mushroom',1,'2024-03-21 07:47:40.112877'),
 (6,'Amanita phalloides','Amanita phalloides , commonly known as the death cap, is a deadly poisonous basidiomycete fungus, one of many in the genus Amanita. Widely distributed across Europe, but introduced to other parts of the world since the late twentieth century A. phalloides forms ectomycorrhizas with various broadleaved trees. In some cases, the death cap has been introduced to new regions with the cultivation of non-native species of oak, chestnut, and pine. The large fruiting bodies (mushrooms) appear in summer and autumn; the caps are generally greenish in colour with a white stipe and gills. The cap colour is variable, including white forms, and is thus not a reliable identifier.','It was traditionally used as an insecticide. The cap was broken up and sprinkled into saucers of milk. It''s known to contain ibotenic acid, which both attracts and kills flies – which gave it its name. Its gills are closely packed and not joined to the stem.','images/plants/mushroom-nun_Amanita_phalloides.JPG','Mushroom',0,'2024-03-21 07:49:09.823530'),
 (7,'Mint','Mints are aromatic, almost exclusively perennial herbs. They have wide-spreading underground and overground stolons and erect, square, branched stems. Mints will grow 10–120 cm (4–48 inches) tall and can spread over an indeterminate area. Due to their tendency to spread unchecked, some mints are considered invasive.

The leaves are arranged in opposite pairs, from oblong to lanceolate, often downy, and with a serrated margin. Leaf colors range from dark green and gray-green to purple, blue, and sometimes pale yellow.

The flowers are produced in long bracts from leaf axils. They are white to purple and produced in false whorls called verticillasters. The corolla is two-lipped with four subequal lobes, the upper lobe usually the largest. The fruit is a nutlet, containing one to four seeds.','Mint leaves create a cool sensation in the mouth. Toothpaste, mouthwash, breath mints, and chewing gum are all commonly flavored with mint. In addition to freshening breath, mint adds flavor to foods and drinks – everything from ice cream and tarts to lemonade and cocktails to meat dishes','images/plants/herb_mint.png','Herb',1,'2024-03-21 07:51:47.474983'),
 (11,'Aubergine','The aubergine is a delicate, tropical perennial plant often cultivated as a tender or half-hardy annual in temperate climates. The stem is often spiny. The flowers are white to purple in color, with a five-lobed corolla and yellow stamens. Some common cultivars have fruit that is egg-shaped, glossy, and purple with white flesh and a spongy, "meaty" texture. Some other cultivars are white and longer in shape. The cut surface of the flesh rapidly turns brown when the fruit is cut open.','Great at soaking up flavours, aubergine works well in stews, salads and curries. Try them baked, grilled or barbecued as a veggie main or in side dishes. If you enjoy our aubergine recipes, why not try some of our delicious vegetarian recipes, freezable vegetarian recipes and Mediterranean recipes.','images/plants/Aubergine.png','Vegetables',1,'2024-03-24 09:00:11.991870');
INSERT INTO "main_comment" ("id","content","comment_date","user_id","plant_id") VALUES (1,'great herb','2024-03-24 11:38:12.658371',2,7);
CREATE INDEX IF NOT EXISTS "main_comment_user_id_cf3356a1" ON "main_comment" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "main_comment_plant_id_6fa99c55" ON "main_comment" (
	"plant_id"
);
COMMIT;
