# The Burnt Book

## Overview

"The Burnt Book" is a web application designed for students to anonymously share gossip about their peers. The purpose is to create a platform for gaining insights into the daily lives of fellow students. Users can submit gossip entries and confirm or deny the accuracy of submitted gossip.

## How to Run

To run the application, follow these steps:

1. **Clone the Repository:**
    ```bash
    git clone <repository_url>
    ```

2. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up Database Configuration:**
    - If using PostgreSQL, set the following environment variables:
        - `DB_TYPE=PG`
        - `PG_USER=<your_pg_user>`
        - `PG_PASSWORD=<your_pg_password>`
        - `PG_HOST=<your_pg_host>`
        - `PG_PORT=<your_pg_port>`

4. **Run the Application:**
    ```bash
    streamlit run app.py
    ```

5. **Access the Application:**
    Open your web browser and navigate to the provided URL (usually http://localhost:8501).

## Features

- **Anonymous Gossip Submission:** Users can submit gossip entries without revealing their identity.
- **Confirmation System:** Peers can confirm or deny the accuracy of submitted gossip entries.
- **Real-time Updates:** The application provides real-time updates as users interact with the platform.

## Lessons Learned

While developing "The Burnt Book," the following lessons were learned:

- **Database Connection:** Handling database connections, especially when using different database systems like SQLite and PostgreSQL, requires careful consideration.
  
- **Streamlit Usage:** Understanding and utilizing the Streamlit library for building web applications quickly.
  
- **UI/UX Design:** Balancing simplicity with an engaging user interface for an intuitive user experience.

## Technologies Used

- Python
- Streamlit
- SQLite (for local development)
- PostgreSQL (for production)

## Questions/Future Improvements

If you have any questions or suggestions for future improvements, feel free to reach out. Potential enhancements include:

- **User Authentication:** Implementing user authentication to ensure secure and private interactions.
  
- **Enhanced UI/UX:** Improving the user interface and experience for a more engaging platform.

## Security Considerations

Ensure that sensitive information such as database credentials and connection details are handled securely and kept confidential.

---

**Note:** Replace `<repository_url>`, `<your_pg_user>`, `<your_pg_password>`, `<your_pg_host>`, and `<your_pg_port>` with actual values.```

Remember to replace placeholder values with your actual repository URL and database credentials. Feel free to tailor the content further to match the specific details and features of your application.
