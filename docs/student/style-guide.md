# Documentation Style Guide  
### Stage 6 Software Engineering — Sydney Technical High School

This style guide defines how you should write technical documentation for the Software Engineering course.  
Clear, consistent documentation is a core professional skill and is assessed throughout the project.

---

## 1. Purpose of Documentation

Your documentation must:

- Explain your system clearly and accurately  
- Support maintainability and future development  
- Demonstrate your understanding of software engineering principles  
- Provide evidence of your design and decision‑making  

Write for a technical audience: senior students, teachers, and developers.

---

## 2. Structure and Organisation

Each page should follow this structure:

1. **Title**  
2. **Purpose / Overview**  
3. **Technical Detail**  
4. **Examples or Diagrams**  
5. **Notes, Limitations, or Assumptions**  
6. **References (if needed)**  

Use headings (`##`, `###`) to break up content logically.

---

## 3. Writing Style

### 3.1 Clarity
- Use short, direct sentences.  
- Avoid unnecessary jargon.  
- Define technical terms when first introduced.

### 3.2 Precision
- Be specific about behaviour, inputs, outputs, and constraints.  
- Avoid vague phrases like “it works” or “it does stuff”.

### 3.3 Professional Tone
- No slang.  
- No conversational filler.  
- No first‑person unless describing your design decisions.

Example:

> “The service worker implements a cache‑first strategy for static assets to reduce load times.”

---

## 4. Markdown Conventions

### 4.1 Code Blocks
Use fenced code blocks with language labels:

````markdown
```python
def example():
    return "hello"
```
````

will look like this with colour coding for your Python...

```python
def example():
    return "hello"
```


### 4.2 Diagrams
Use Mermaid for diagrams:
#### Flowcharts

````markdown
```mermaid
flowchart TD
    A[Request] --> B[Service Worker]
    B --> C[Cache]
    B --> D[Network]
```
````

will render into this!

```mermaid
flowchart TD
    A[Request] --> B[Service Worker]
    B --> C[Cache]
    B --> D[Network]
```

#### Entity Relationship Diagrams: to show a database schema with entities/tables and relationships

This uses markdown mermaid to create a diagram of your database schema.
This diagram shows how the main tables in your project relate to each other.  
It uses **Mermaid ERD syntax**, which GitHub renders automatically.
*A visual overview of the relational model used in this template*

````markdown
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
````

to render as this...

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

#### Class Diagrams: to objected oriented design, data dictionaries, entities, attributes and attribute types

````markdown
``` mermaid
classDiagram
  Person <|-- Student
  Person <|-- Professor
  Person : +String name
  Person : +String phoneNumber
  Person : +String emailAddress
  Person: +purchaseParkingPass()
  Address "1" <-- "0..1" Person:lives at
  class Student{
    +int studentNumber
    +int averageMark
    +isEligibleToEnrol()
    +getSeminarsTaken()
  }
  class Professor{
    +int salary
  }
  class Address{
    +String street
    +String city
    +String state
    +int postalCode
    +String country
    -validate()
    +outputAsLabel()
  }
```
````

renders beautifully as this ...

``` mermaid
classDiagram
  Person <|-- Student
  Person <|-- Professor
  Person : +String name
  Person : +String phoneNumber
  Person : +String emailAddress
  Person: +purchaseParkingPass()
  Address "1" <-- "0..1" Person:lives at
  class Student{
    +int studentNumber
    +int averageMark
    +isEligibleToEnrol()
    +getSeminarsTaken()
  }
  class Professor{
    +int salary
  }
  class Address{
    +String street
    +String city
    +String state
    +int postalCode
    +String country
    -validate()
    +outputAsLabel()
  }
```





## 4.3 Admonitions
Use admonitions for emphasis:

````markdown
!!! note "Note"

    This endpoint requires authentication.
````


will look like:

```
!!! note "Note"

    This endpoint requires authentication.
```

