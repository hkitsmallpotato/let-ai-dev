# StarCoder/StarChat Forum DB Schema Design

This is the one example where StarChat's performance is scarily good. In just about 30 seconds total over 3 turn of very simple prompt it:

- Explained verbally how to desgin the DB Schema
- Provide SQL file to create all the tables
- Give a high level ER diagram

## Prompts

- Suggest a DB schema design (RDBMS) for a forum.
- Given your suggestion above, show me the code for SQL file to create the tables implementing it.
- Show me the code in mermaid or plantUML or other language you find appropiate to display an ER diagram illustrating the schema above.

## AI Answer

### Verbal description

Here is an example of the database schema for a simple forum:

1. User table with columns id, name and email address. 
2. Post table with columns id, title, content, user_id, created_at and updated_at. The post should be associated to one user through this foreign key column. 
3. Comment table with columns id, content, post_id, user_id, created_at and updated_at. The comment also needs to reference the post it belongs too using another foreign key column. 
4. Like table with columns id, post_id, user_id and created_at. This will store information about which users liked what posts. 
5. Tagging system - we can add additional tables like tag or category that would allow us to categorize our posts into different topics/categories. For simplicity let’s assume there are only two categories: “Announcements” and “Help”. We could then have 2 more tables: CategoryPostMapping and TagPostMapping where each row in these mapping tables links a specific category or tag to a particular post. 
6. Finally, we need some way to track who has access to modify which data. Let’s say we want to create roles such as Moderator, Admin etc. Then we can introduce another table called RoleUserMapping that stores mappings between users and their respective role(s). In addition to this, we may want to log all changes made to the database so that we know who did what when. To do this we can use yet another table called AuditLog that contains timestamp, username, action type and primary key of the changed record.

This covers most basic requirements for a functional forum including authentication, authorization, creating threads, replies, likes, tags & categories. Additional features like search functionality, reporting comments etc., require additional tables and logic but those are out-of-scope for now.

### SQL file

Sure! Here’s an example script you can run against any MySQL compatible RDBMS server to generate the necessary tables based on my previous response:

```sql
    CREATE TABLE `user` (
      `id` int NOT NULL AUTO_INCREMENT PRIMARY KEY,
      `name` varchar(20),
      `email` VARCHAR(50) UNIQUE 
    );
    
    CREATE TABLE `post` (
      `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
      `title` TEXT,
      `content` MEDIUMTEXT,
      `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP(),
      `updated_at` TIMESTAMP ON UPDATE CURRENT_TIMESTAMP(),
      FOREIGN KEY (`user_id`) REFERENCES `user`(`id`)
    );
    
    CREATE TABLE `comment` (
      `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
      `content` MEDIUMTEXT,
      `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP(),
      `updated_at` TIMESTAMP ON UPDATE CURRENT_TIMESTAMP(),
      `post_id` INT,
      FOREIGN KEY (`post_id`) REFERENCES `post`(`id`),
      FOREIGN KEY (`user_id`) REFERENCES `user`(`id`)
    );
    
    CREATE TABLE `like` (
      `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
      `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP(),
      `post_id` INT,
      FOREIGN KEY (`post_id`) REFERENCES `post`(`id`),
      FOREIGN KEY (`user_id`) REFERENCES `user`(`id`)
    );
    
    CREATE TABLE `category` (
      `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
      `name` VARCHAR(20)
    );
    
    CREATE TABLE `tag` (
      `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
      `name` VARCHAR(20)
    );
    
    CREATE TABLE `category_mapping` (
      `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
      `category_id` INT,
      `post_id` INT,
      FOREIGN KEY (`category_id`) REFERENCES `category`(`id`),
      FOREIGN KEY (`post_id`) REFERENCES `post`(`id`)
    );
    
    CREATE TABLE `tag_mapping` (
      `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
      `tag_id` INT,
      `post_id` INT,
      FOREIGN KEY (`tag_id`) REFERENCES `tag`(`id`),
      FOREIGN KEY (`post_id`) REFERENCES `post`(`id`)
    );
    
    CREATE TABLE `role` (
      `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
      `name` VARCHAR(20)
    );
    
    CREATE TABLE `user_role_mapping` (
      `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
      `user_id` INT,
      `role_id` INT,
      FOREIGN KEY (`user_id`) REFERENCES `user`(`id`),
      FOREIGN KEY (`role_id`) REFERENCES `role`(`id`)
    );
    
    CREATE TABLE `audit_log` (
      `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
      `timestamp` TIMESTAMP DEFAULT CURRENT_TIMESTAMP(),
      `username` VARCHAR(20),
      `action_type` ENUM('create', 'update', 'delete'),
      `record_id` INT,
      INDEX idx_record_id (record_id),
      CONSTRAINT fk_record
        FOREIGN KEY (record_id) 
        REFERENCES <table>(id)
    );
```

Note that I’ve included indices and constraints to optimize querying performance later if needed. You’ll likely want to adjust field lengths / types depending on your own usage patterns.

### ER Diagram

Here is an example Mermaid syntax:
```
erDiagram
  USER ||--o{ POST : "has many"
  USER }|--|{ ROLE : "belongs to"
  POST }|..|{ COMMENT : "has many"
  LIKE ||--|| POST : "likes"
  CATEGORY }o--o{ POST : "is part of"
  TAG }o--o{ POST : "is tagged with"
```

