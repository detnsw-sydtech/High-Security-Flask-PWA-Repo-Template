# Entity Relationship Diagram (ERD)
*A visual overview of the relational model used in this template*

This diagram shows how the main tables in your project relate to each other.  
It uses **Mermaid ERD syntax**, which GitHub renders automatically.


```mermaid
erDiagram

    ROLE ||--o{ USER : "has many"
    USER }o--|| ROLE : "belongs to"

    ITEMTYPE ||--o{ ITEM : "has many"
    ITEM }o--|| ITEMTYPE : "belongs to"

    ITEM ||--o{ ITEM_CREATOR : "links"
    CREATOR ||--o{ ITEM_CREATOR : "links"

    ITEM ||--o{ ITEM_CATEGORY : "links"
    CATEGORY ||--o{ ITEM_CATEGORY : "links"

    ROLE {
        int id PK
        string name
    }

    USER {
        int id PK
        string username
        string email
        string password_hash
        int role_id FK
        datetime created_at
    }

    ITEMTYPE {
        int id PK
        string name
        string description
    }

    ITEM {
        int id PK
        string title
        text description
        int year
        string identifier
        int item_type_id FK
        text internal_notes
        datetime created_at
        datetime updated_at
    }

    CREATOR {
        int id PK
        string name
        int birth_year
        int death_year
    }

    CATEGORY {
        int id PK
        string name
    }

    ITEM_CREATOR {
        int item_id FK
        int creator_id FK
    }

    ITEM_CATEGORY {
        int item_id FK
        int category_id FK
    }
```
