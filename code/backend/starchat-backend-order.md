# StarCoder/StarChat Microservice Implementation test (part 1)

(Experiment to extend the automation from design to actual coding phase using the food ordering and delivery platform as an example)

(Output manually cleaned and curated)

StarChat performed reasonably well on the first part of this test where I asked it to implement the part of the ordering microservice with non-trivial domain logic.

## Prompts

**Initial prompt**:

We are working on this project:

{project}

{memo}

Microservice architecture is used for the backend. Techstack is fastify + prisma connecting to postgreSQL.

Implement this microservice: 

Order Placement Interface – Allows users to browse available dishes, place orders, select preferred pickup / delivery option, enter billing address, complete transaction via secure gateway integration. 

Work step by step and begin by designing the database scheme, listing all entities and their relations that is minimally needed to implement the order placement microservice just described, and then give a prisma schema.

**Refined prompt (describe the change from initial prompt)**:

(same element omitted)

(We first added text to describe all microservice in the architecture to give better context)

List of microservices: {list-of-microservice}

(Then we reworded slightly)

Let's implement the Order Placement microservice first.

Work step by step and begin by designing the database scheme, listing all entities and their relations that is minimally needed to implement the order placement microservice just described, and then give a prisma schema.

**Step 2 prompt**:

(similar context text as above)

Work step by step and now let’s move on to implement it in fastify + prisma. *Show me codes implementing this API with their domain logic, while omitting authentication as it will be implemented by another team member.* For reference, below is the prisma scheme design (possibly incomplete):

{prisma-schema}

## AI answer

**Initial answer**:

Here’s an example of what your Prisma Schema could look like based off of our use case description:

```
datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}
generator client {
  provider        = "prisma-client-js"
  previewFeatures = ["interactiveTransactions"]
}
model User {
    id Int @id @default(autoincrement())
    name String?
    email String @unique
    passwordString String 
    saltString String // Salt value stored in base64 encoding format
    phone String?
    profilePicUrl String?
    coverPhotoUrl String?
    biography Text?

    createdOn DateTime @default(now())
    updatedOn DateTime @updatedAt
    
    // Relationships
    cart Cart?
    favorites Favorite[]
    reviews Review[]
}
//... other models omitted for brevity...
```

This model would be implemented using PostgreSQL as the underlying data store. The User model has various fields including basic user information (name, email, etc.), authentication credentials (password/salt), contact details (phone number, etc.), images URLs (profile picture URL, cover photo URL) and more. You may also notice there are relationships between different models - e.g., each User has many Cart, Favorite, and Review. This allows you to easily query related records without having to make multiple requests to the DB. Additionally, Prisma supports advanced features such as transactions, filtering, pagination, sorting, aggregations, and much more!

**Refined answer**:

Here’s an example Prisma Schema for our “Order Placing” Microservice:

```
type User { id: ID! @id name: String email: String! @unique passwordHash: String
orders: [Order] }
type Dish { id: ID! @id title: String description: String price: Float imageURL: String restaurantId: Int menuSection: String calories: Float allergens: [String!]
reviews: [Review] }
type OrderStatusHistoryEntry { status: OrderStatusType timestamp: DateTime! }
enum OrderStatusType { PENDING PREPARING READY_FOR_PICKUP ON_THE_WAY DELIVERED CANCELLED }
type Address { streetAddress: String city: String state: String country: String postalCode: String }
type Order { id: ID! @id placedAt: DateTime! totalPrice: Float customerName: String customerEmail: String shippingAddress: Address items: [OrderItem] statusHistories: [OrderStatusHistoryEntry] driverId: Driver @relation(fields: [driverId], references: [id]) restaurantId: Restaurant @relation(fields: [restaurantId], references: [id]) }
model OrderItem { quantity: Int unitPrice: Float discountPercentage: Float subtotal: Float orderId: Int dishId: Int
@@index([dishId], name: “DishIndex”) @@map(“orderitem”) }
model Review { rating: Int comment: String authorName: String authorType: AuthorType reviewDate: DateTime dishId: Int
@@index([dishId], name: “DishIndex”) @@map(“review”) }
enum AuthorType { CUSTOMER RESTAURANT }
type Restaurant { id: ID! @id name: String address: String phoneNo: String websiteUrl: String averageRating: Float numberOfRatings: Int coverImage: Image menuItems: [MenuItem] openingHours: OpeningHour[]
@@map(“restaurant”) }
type MenuItem { id: ID! @id category: Category itemName: String itemDescription: String price: Float course: Course ingredients: [Ingredient] spicyLevel: SpicyLevel allergyInfo: AllergyInformation mainCourse: Boolean sideDishes: [SideDish] drinkOptions: [DrinkOption] additionalNotes: AdditionalNotes photos: [Photo] reviews: [Review] restaurantId: Int
@@map(“menuitem”) }
enum Category { APpetizers MainCourses Salads Sandwiches Wraps Burgers Fries Shakes Sides Beverages }
enum Course { Entree Side Appetizer Desert }
type Ingredient { ingredientName: String amount: String measurementUnit: MeasurementUnit }
enum MeasurementUnit { oz g ml l pcs tbsp Tbsp cup cups pinch teaspoon tablespoons dash slices pieces 1/2 1/4 quarter eighth double portion small medium large extra large half dozen three quarters sixteen eighteen twenty four forty fifty hundred thousand five hundred two hundred million billions trillions quadrillions sextillions octillions nonillion decillion undecillion duodecillion tredecillion quatttuordecillion quinquagintillion sexagintillion septemvigintillion octogintillion novemvigintillion trigintillion untrigintillion duotrigintillion trestrigintillion quattuortrigintillion quadragintillion quinquatrigintillion sexatrigintillion septenmtrigintillion octotrigintillion noventrigintillion centillion }
enum SpicyLevel { NotSpicy Mild Medium Hot VeryHot }
type AllergyInformation { containsGluten: Boolean containsLactose: Boolean otherAllergiesAndAdverseReactions: String
```

**Backend code**:

Here’s an example implementation for creating a new order using Fastify and Prisma Client:

```javascript 
const fastify = require(‘fastify’)({ logger: true }); 
const axios = require(‘axios’); // Used for making HTTP requests 
// Set up database connection 
const prisma = new PrismaClient();
// Define routes 
fastify.get(‘/orders’, async function (request, reply) { const orders = await prisma.order.findMany({}); return orders; });
fastify.post(‘/orders’, async function (req, res) => { try{ const body = req.body;
    if (!isValidRequestBody(body)) {
        throw new Error("Invalid request body");
      }

      const userExists = await doesUserExist(body.customerEmail);
      if (!userExists) {
        throw new Error(`User with email ${body.customerEmail} not found`);
      }

      const existingRestaurant = await getRestaurantById(body.restaurantId);
      if (!existingRestaurant) {
        throw new Error(`Restaurant with ID ${body.restaurantId} not found`);
      }

      const orderItems = [];
      for (let i=0;i<body.items.length;i++) {
          const orderItemBody = body.items[i];
          const dish = await getDishByTitle(orderItemBody.title);
          if (!dish) {
            throw new Error(`Dish with title '${orderItemBody.title}' not found`);
          } else if (dish.restaurantId!== parseInt(body.restaurantId)) {
              throw new Error(`Dish with title '${orderItemBody.title}' doesn't belong to restaurant with ID ${body.restaurantId}`);
          }

          const orderItem = {
              quantity: orderItemBody.quantity,
              unitPrice: dish.price,
              discountPercentage: calculateDiscountPercentage(orderItemBody),
              subtotal: calculateSubTotal(
                  orderItemBody.quantity, 
                  dish.price, 
                  calculateDiscountPercentage(orderItemBody)),
          };
          orderItems.push(orderItem);
      }

      const order = {
        placedAt: new Date(), 
        totalPrice: calculateTotalPrice(orderItems), 
        customerName: getUserFullName(body.customerEmail), 
        customerEmail: body.customerEmail, 
        shippingAddress: body.shippingAddress 
      };

      const createdOrder = await createOrder(order, orderItems);
      return res.status(201).send(createdOrder);
  } catch (error) {
    console.log(error.message);
    return res.status(500).send({ message: error.message });
  }
});
async function isValidRequestBody(body) { return!!body.customerEmail && Array.isArray(body.items) && body.items.every((item) => typeof item === ‘object’ && ‘title’ in item && ‘quantity’ in item ); };
function getUserFullName(email) { /* Implementation omitted */ }; 
async function doesUserExist(email) { const user = await prisma.user.findFirst({ where: { email: email } }); return!!user; };
async function getRestaurantById(id) { const restaurant = await prisma.restaurant.findUnique({where : {id: id}, include:{menuItems:true}}); return restaurant? restaurant : null ; };
async function getDishByTitle(title){ const dish = await prisma.dish.findUnique({ where: { title: title }, include: { reviews: true } }) return dish?dish:null; }
function calculateDiscountPercentage(orderItem) { /* Implementation omitted */} 
function calculateSubTotal() {/Implementation omitted/} 
function calculateTotalPrice(){/Implementation omitted/}
async function createOrder(order, orderItems) { const transaction = await prisma.$transaction(async () => { const createdOrder = await prisma.order.create({ data: order });
const createdOrderItems = []
for (let i=0;i<orderItems.length;i++) {
  const orderItemData = Object.assign({}, orderItems[i]);
  delete orderItemData.orderId;

  const createdOrderItem = await prisma.orderItem.create({
    data: {
     ...orderItemData,
      order: { connect: { id: createdOrder.id }}
    }
  });
  
  createdOrderItems.push(createdOrderItem);
}

return createdOrder;
});
return transaction; }
```

Now you can start your server like so: `node index.js` And test out these endpoints via curl or any other tool that supports sending HTTP requests.

**Schema correction**:

Here’s an updated version of the Prisma Schema that includes the Menu entity and its relationships to both Restaurant and Dish:
```
// Define your data model here using Prisma syntax
model Restaurant {
  //...other fields...

  menus   Menus?    @relation("RestaurantToMenus")
  dishes  Dishes[]  @relation("RestaurantToDishes")
}

model Dish {
  //...other fields...
  
  restaurants     Restaurants[]      @relation("RestaurantToDishes", references: "id")
  menuSections    MenuSections[]     @relation("MenuSectionsToDishes")
  
}


model Menu {
    id              Int               @default(autoincrement()) @id 
    createdAt       DateTime          @default(now())
    updatedAt       DateTime          @updatedAt

    section         MenuSection?      @relation("MenuSectionsToMenus")
    dishes          Dishes[]          @relation("MenuSectionsToDishes")
    
    published       Boolean           @default(false)
    
}



enum MenuSection{
    appetizers, salad, sandwich, wrap, burger, fry, sides, drinks
}
```
