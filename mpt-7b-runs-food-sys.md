# MPT-7b runs on a Food ordering and delivery platform (part 2)

Second run done on 19th May, 2023.

## Top level System Architecture

Sure! Here’s my proposal for the top-level architecture using a light version of the C4 framework:

In this architecture, we have three main layers: physical, conceptual, and implementation/code. The physical layer represents the actual servers/VM/container/network. This layer includes all the infrastructure required to run the application, such as servers, storage, network, and security.

The conceptual layer represents the business logic and rules of the application. It defines how the different modules/components/microservices interact with each other and how they fulfill the requirements of the stakeholders. In this case, there would be two primary concepts: User and Restaurant. A user would create an account, log in, search for restaurants, view menus, place orders, and pay. A restaurant would register, add menus, receive orders, prepare food, accept payments, and communicate with delivery services if necessary.

Finally, the implementation/code layer consists of the module/component/microservice/monolith that implements the functionalities defined in the conceptual layer. Each microservice would be responsible for a specific task, such as user authentication, restaurant registration, menu management, order fulfillment, payment processing, etc. These microservices would communicate with each other through APIs to ensure smooth operations.

For the frontend component, we would use ReactJS to build a responsive and interactive user interface. We would integrate it with the backend using RESTful APIs. For the database, we would use MongoDB to store all the relevant data. Finally, we would deploy the entire solution on AWS EC2 instances for scalability and reliability purposes.

Please let me know if you have any further clarifications or questions regarding this architecture.

## Backend System Design

Thank you for providing me with the background information about the project. Based on the requirements mentioned earlier, here’s my suggestion for the tech stack for the backend components:

**Tech Stack:**
- Backend: Node.js (Express.js)
- Database: MongoDB
- ORM: Mongoose
- Authentication: Passport.js
- Authorization: JSON Web Tokens (JWT)
- Messaging: RabbitMQ
- Load Balancing: Nginx
- Caching: Redis
- Monitoring: Nagios/Zabbix
- Deployment: Docker/Kubernetes

**High Level DB Schema Design:**

We’ll need to define several entities in our database schema, based on the requirements of the application. Some examples include:

User Entity:
- username
- email
- password
- firstName
- lastName

Restaurant Entity:
- name
- location
- cuisineType
- menuItems

Order Entity:
- userId
- restaurantId
- orderDate
- totalAmount
- paidAmount
- deliveryStatus

Payment Entity:
- userId
- orderId
- paymentMethod
- paymentDate
- amountPaid

Delivery Service Entity:
- serviceProviderId
- restaurantId
- deliveryAddress
- deliveryDate

Relationships:
- One-to-many relationship between User and Order entity
- Many-to-one relationship between Restaurant and Order entity
- Many-to-one relationship between Restaurant and Payment entity

**API Design:**

Here’s a sample set of endpoint groups and their corresponding actions:

Authentication Endpoints:

- `POST /users/register` - Registers new user credentials
- `POST /users/login` - Logins existing user credentials

Authorization Endpoints:

- `GET /restaurants/{restaurantId}/menu` - Retrieves list of menu items from specified restaurant
- `PUT /orders/{orderId}` - Updates order details


Menu Endpoint Group:

- `GET /menus` - Retrieves list of all active restaurants’ menus
- `GET /menus/{restaurantId}` - Retrieves detailed info about specified restaurant’s menu
- `DELETE /menus/{restaurantId}` - Removes selected item from specified restaurant’s menu



Order Fulfillment Endpoint Group:

- `GET /orders/{orderId}/deliveries` - Retrieves current state of ordered item
- `POST /orders/{orderId}/payments` - Pays remaining balance due on particular order
- `DELETE /orders/{orderId}` - Confirms cancellation of open order



Messaging Endpoint Groups:

- `GET /messages` - Displays recent messages exchanged within app
- `POST /sendMessage` - Sends direct messaging request to another party inside app
- `GET /receivedMessages/{messageId}` - Retrieves previously received messages containing certain keywords
- `Delete /sentMessages/{messageId}` - Purges old draft copies of outgoing messages after 24 hours


Monitoring Endpoint Group:

- `GET /status` - Checks overall health and wellbeing of server resources
- `POST /alerts` - Reports critical issues requiring immediate attention
- `GET /logs` - Display historical records of past events affecting server operation

Overall, these endpoints cover most common scenarios needed throughout the lifecycle of the application, ensuring proper communication flows while maintaining appropriate authorization control measures at all stages. Additionally, integrating monitoring tools like Zabbix into the deployment pipeline ensures continuous improvement of server efficiency over time.