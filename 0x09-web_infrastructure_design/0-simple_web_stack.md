# Simple Web Stack Infrastructure

![Simple Web Stack](0-simple_web_stack.jpg)

## Infrastructure Design

The provided image illustrates a basic one-server web infrastructure that hosts a website reachable via www.foobar.com. Below is an explanation of the various components and their roles in this infrastructure:

1. **User's Computer**:
   - Represents the device from which a user accesses the website.
   
2. **Domain Name (foobar.com)**:
   - Acts as the human-readable alias for the server's IP address (8.8.8.8).
   - Allows users to access the website using the memorable name www.foobar.com.
   
3. **DNS Server**:
   - Resolves domain names to IP addresses.
   - Maps the domain foobar.com to the server's IP address (8.8.8.8).
   
4. **Server (8.8.8.8)**:
   - Hosts all components of the web infrastructure.
   - Runs the web server, application server, and database.
   
5. **Web Server (Nginx)**:
   - Handles incoming HTTP requests from clients.
   - Serves static content efficiently and can act as a reverse proxy for dynamic content.
   
6. **Application Server**:
   - Executes application logic and generates dynamic content based on user requests.
   - Hosts the application codebase.
   
7. **Database (MySQL)**:
   - Stores and manages website data, such as user accounts, content, and configurations.

## Explanation of Specifics

- **Server**: A computer system responsible for processing requests from clients and serving them with required resources.

- **Domain Name**: Provides a human-readable address for accessing websites, acting as an alias for server IP addresses.

- **www Record**: A CNAME DNS record that points to the root domain record, allowing traffic redirection from www.foobar.com to foobar.com.

- **Web Server**: Handles incoming HTTP requests, serving static content efficiently, and routing dynamic content requests to the application server.

- **Application Server**: Hosts dynamic components of the website, executing application logic and generating content dynamically.

- **Database**: Stores and manages website data, enabling retrieval and manipulation of information as required.

## Issues with the Infrastructure

1. **Single Point of Failure (SPOF)**:
   - Since all components are hosted on a single server, any failure can lead to downtime for the entire website.

2. **Downtime During Maintenance**:
   - Maintenance tasks such as deploying new code may require restarting the web server, resulting in downtime for users.

3. **Scalability Limitations**:
   - A single server may not efficiently handle increased traffic, limiting scalability options without additional servers or load balancing mechanisms.
