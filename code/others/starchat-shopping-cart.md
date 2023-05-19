# StarCoder/StarChat Shopping cart test

Note: for relatively standard coding task like this, ability to follow instruction is more important than raw knowledge/skill, so other AI like Vicuna seems to perform better on this one.

(Output manually cleaned and curated)

## Schema Design Task

### Initial prompt

Show me a sample `prisma.schema.json` file using a shopping cart app as example. There should be modelling for product catalog, cart, and user.

(Subsequent prompt omitted)

### AI answer

```
model Product {
  id          Int      @default(autoincrement()) @id
  name        String? 
  description String? 
  price       Float?  
  images      Json?   

  @@map("products")
}

model User {
  id            Int           @default(autoincrement()) @id
  email         String        @unique
  password      <PASSWORD>
  name          String?
  orders        Order[]       @relation("UserOrders")
  createdAt     DateTime?     @default(now())
  
  @@map("users")
}


model CartItem {
  id             Int              @default(autoincrement()) @id
  productId      Int              @map("product_id") // Note that we're using `@@map` to specify how this field maps to the "product_id" column in our database table. This allows us to use snake case when writing SQL queries but have camelCase fields in our TypeScript/JavaScript code.
  quantity       Int?
  subTotal       Float?
  tax            Float?
  total          Float?
  order          Order?           @relation(fields:[orderId], references:[id])
  orderId        Int?             @map("order_id")
  createdAT      DateTime?        @default(now())
  updatedAt      DateTime?        @updatedAt

  @@index([productId], name:"CartItemProductIdIndex")
  @@map("cart_item")
}



// The "@relation" attribute specifies what relationship this model has to another one. In this example it means that each CartItem belongs to exactly one Order via its "order" foreign key relation.
model Order {
  id               Int                 @default(autoincrement()) @id
  items            CartItem[]          @relation("OrderItems")
  user             User                @relation("UserOrders", fields: [userId], references: [id])
  userId           Int                  @map("user_id")
  createdAt        DateTime?           @default(now())
  updatedAt        DateTime?           @updatedAt


  @@map("orders")
}
```

Note that I’ve added some additional attributes like @map, @index,@default, etc., to provide more information about my data model to Prisma. You can read more about these at https://www.prisma.io/docs/reference/api-reference/prisma-schema-file#attributes.

(I compacted the json for convinience to myself)

```json
[{"name":"Product","properties":{"id":{"type":"integer","autoIncrement":true,"primaryKey":true},"name":{"type":"string"},"description":{"type":"string"},"price":{"type":"float"},"images":{"type":"json"}},"fields":[{"name":"id","type":"integer"},{"name":"name","type":"string"},{"name":"description","type":"string"},{"name":"price","type":"float"},{"name":"images","type":"json"}]},{"name":"CartItem","properties":{"id":{"type":"integer","autoIncrement":true,"primaryKey":true},"productId":{"type":"integer","references":{"Product":"id"}},"quantity":{"type":"integer"},"subtotal":{"type":"float"},"tax":{"type":"float"},"total":{"type":"float"},"createdAt":{"type":"datetime"},"updatedAt":{"type":"datetime"}},"fields":[{"name":"id","type":"integer"},{"name":"productId","type":"integer"},{"name":"quantity","type":"integer"},{"name":"subtotal","type":"float"},{"name":"tax","type":"float"},{"name":"total","type":"float"},{"name":"createdAt","type":"datetime"},{"name":"updatedAt","type":"datetime"}]},{"name":"User","properties":{"id":{"type":"integer","autoIncrement":true,"primaryKey":true},"name":{"type":"string"},"email":{"type":"string"},"password":{"type":"string"},"createdAt":{"type":"datetime"},"orders":{"type":"relation","relation":"Order","fields":[{"name":"userId","type":"integer"}]}},"fields":[{"name":"id","type":"integer"},{"name":"name","type":"string"},{"name":"email","type":"string"},{"name":"password","type":"string"},{"name":"createdAt","type":"datetime"},{"name":"orders","type":"relation","relation":"Order","fields":[{"name":"userId","type":"integer"}]}]},{"name":"Order","properties":{"id":{"type":"integer","autoIncrement":true,"primaryKey":true},"user":{"type":"User","relation":"User","fields":[{"name":"userId","type":"integer"}]},"items":{"type":"CartItem[]","relation":"CartItem","fields":[{"name":"cartItems","type":"CartItem[]"}]},"createdAt":{"type":"datetime"},"updatedAt":{"type":"datetime"}},"":""}]
```

## Backend Coding task

### Prompts

**Take 1**:

Context: This is a Proof of concept demo app in an IT bootcamp. Show me the code to implement basic CRUD on the storefront for a customer to add products to carts. Use RESTful API style. Also add authentication by JWT.

**Take 2**:

Context: This is a Proof of concept demo app in an IT bootcamp. Our project is a shopping cart app with fastify + prisma connecting to postgreSQL. Show me the code to implement basic CRUD on the storefront for a customer to add products to carts and similar operations. Use RESTful API style. Skip authentication for now. The code show be concise. Assume the following prisma schema:
{schema}


### AI answer

**Take 2**

Sure, here’s some sample code that demonstrates how you could create a simple “shopping cart” application using Fastify and Prisma. It includes routes for creating/fetching/updating/deleting items from a user’s cart as well as retrieving all available products. Note that this is just a starting point - there are many additional features (such as validation, error handling etc.) which can be added based on your specific requirements. Also note that I’ve omitted any authentication logic since it isn’t relevant to the core functionality of the app.

```js
const fastify = require('fastify')({ logger: true });
const { PrismaClient } = require('@prisma/client'); // Import the Prisma client library
const productData = [
  { id: 1, name: 'Shoes', price: 90 }, 
  { id: 2, name: 'Pants', price: 35 }, 
  { id: 3, name: 'Hat', price: 48 }, 
  { id: 4, name: 'Gloves', price: 67 }, 
  { id: 5, name: 'Sunglasses', price: 25 }, 
];
// Create a new instance of the Prisma Client
const prisma = new PrismaClient();
async function main() {
  await prisma.$connect(); // Connect to the database

  const getProductsHandler = async () => {
    return JSON.stringify(await prisma.product.findMany());
  };
  
  const createCartItemHandler = async ({ body }) => {
    try{
      if (!body ||!body.productId) throw Error("Invalid request");

      let existingProduct = await prisma.product.findFirst({
        where : {
          id : parseInt(body.productId), 
        }
      });
      
      if(!existingProduct){
        throw Error(`No Product found with ID ${body.productId}`); 
      } 

      console.log(`${existingProduct.name} Added`);
      
     /* Add item to Cart */ 
     // Check if User already has a cart or not 
    let currentUserId = 1; // Replace with actual logged-in user ID
    let currentUserCart = await prisma.cart.findFirst({where:{userId:currentUserId}});

    if(!currentUserCart){
      // If no cart exists, create one first before adding item
      currentUserCart = await prisma.cart.create({data:{
        userId:currentUserId,
        totalItems:1,
        subTotalPrice:parseInt(existingProduct.price),
      }})
    }else{
      // Update Total Items & Subtotal Price
      let updatedSubTotalPrice = parseInt(currentUserCart.subTotalPrice)+parseInt(existingProduct.price);
      let updateCurrentCart = await prisma.cart.update({
        data:{
          totalItems:currentUserCart.totalItems+1, 
          subTotalPrice:updatedSubTotalPrice,  
        },
        where:{id:currentUserCart.id},  
      })
    }
    
    // Finally, associate Item with its respective Cart  
    let createdCartItem = await prisma.cartitem.create({
      data:{
        productId:parseInt(body.productId),
        quantity:1,
        cartId:currentUserCart.id,
      }
    })
   .catch((err)=>{throw err});
  
    return `Added ${createdCartItem.quantity} x ${createdCartItem.product.name}`;
   } catch (error) {
     return `${error}` ; 
   }
  };
  
  const deleteCartItemHandler = async ({ params}) => {
    try{
      if (!params ||!params.itemId ) throw Error("Invalid Request") ; 
      
    // Find the associated Cart Item record by Id
    let targetCartItemRecord = await prisma.cartitem.findFirst({
      where:{
        id:parseInt(params.itemId),
      }
    }).catch(()=>{}) ; 

    if(!targetCartItemRecord ){
      throw Error (`No Record Found With Given ID`) ; 
    } else {
      // Get the corresponding Cart details so we can update their totals accordingly
      let parentCartDetails = await prisma.cart.findFirst({
        where:{
          id:targetCartItemRecord.cartId,
        }
      }) ; 

      if(!parentCartDetails){
         throw Error ("Parent Cart Details Not Found!") ; 
      }else{

        // Calculate Updated Quantity & Subtotal Price after deletion of given Cart Item
        let updatedQuantity = parentCartDetails.totalItems - targetCartItemRecord.quantity ; 
        let updatedSubTotalPrice = parentCartDetails.subTotalPrice - (targetCartItemRecord.product.price * targetCartItemRecord.quantity ); 

        // Delete the targeted Cart Item itself
        let deletedTargetedItem = await prisma.cartitem.delete({
          where:{
            id:parseInt(params.itemId),
          }
        }) ;  
        
        // Update Parent Cart records with the latest values
        let
```

(network interruption)

**Take 2 retry**

Here’s some sample code implementing basic Create, Read, Update, Delete (CRUD) functionality for the product resource based off your Prisma schema:




#### Install Fastify & other dependencies
```sh
npm install --save fastify fastify-swagger swagger-ui-dist
```

#### Define routes

```js
const router = require('fastify').Router()

module.exports = async function (fastify, opts) {
  fastify.get('/docs', async (_, reply) => {
    return await reply.send({
      openapi: '3.0.2',
      info: {
        title: 'Fastify Shopping Cart Demo App',
        version: '1.0.0'
      },
      paths: {}
    })
  })

  fastify.register(require('fastify-swagger'), {
    routePrefix: '/docs',
    exposeRoute: true,
    swagger: {
      info: {
        title: 'Fastify Shopping Cart Demo App',
        description: 'A simple demonstration of a shopping cart application built with Fastify and PostgreSQL.',
        contact: {
          name: '<NAME>',
          url: 'https://github.com/johndoe',
          email: '<EMAIL>'
        }
      },
      externalDocs: {
        url: 'https://example.com/',
        description: 'Find more examples here'
      },
      host: 'localhost:8080',
      schemes: ['http'],
      consumes: ['application/json'],
      produces: ['application/json']
    }
  });


  router.post('/products', createProduct);
  router.get('/products/:id', getProductById);
  router.put('/products/:id', updateProduct);
  router.delete('/products/:id', deleteProduct);

  
  
  async function createProduct(req, res) {
    try {
      let newProduct = req.body;
      if (!newProduct ||!newProduct.name || typeof newProduct.price!== 'number') throw Error();
    
      let savedProduct = await fastify.prisma.product.create({ data: newProduct});
      console.log(`Saved ${savedProduct}`);
      res.status(201).send({'message': 'Created'});

    } catch (err) {
      console.error(err);
      res.status(400).send({'message': err.message})
    }
  };


  async function getProductById(req, res) {
    try {
      let foundProduct =  await fastify.prisma.product.findUnique({ where: { id: parseInt(req.params.id)}} );
      if(!foundProduct){
        res.code(404).send({"message": "Not Found"});
      } else{
        res.send(foundProduct);
      }
    
    }catch(e){
      console.error(e);
      res.code(500).send({"message":"Server error"})
    }
  };


  async function updateProduct(req,res){
    try {
      let updatedProductData = req.body;
      let existingProduct = await fastify.prisma.product.update({where:{id :parseInt(req.params.id)},data:updatedProductData});
      if(!existingProduct){
        res.code(404).send({"message": "Not Found"});
      }else{
        res.send(existingProduct);
      }
      
    } catch (e) {
      console.error(e);
      res.code(500).send({"message":"Server error"})
    }
  };


  async function deleteProduct(req,res ){
    try {
      let deletedProductCount =await fastify.prisma.product.deleteMany({where:{id : parseInt(req.params.id)}} );
      if(deletedProductCount.count === 0){
        res.code(404).send({"message": "Not Found"});
      }else{
        res.send({"message":`${deletedProductCount.count} record(s) deleted successfully.`});
      }
      

    } catch (e) {
      console.error(e);
      res.code(500).send({"message":"Server error"})
    }
  };


  fastify.use('/',router )
}
```

This implementation uses Fastify as the web framework and exposes Swagger documentation at `/docs`. You can modify or extend these endpoints further depending on your specific needs.

