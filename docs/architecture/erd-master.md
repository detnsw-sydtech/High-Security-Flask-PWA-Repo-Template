# Master Entity‑Relationship Diagram  
A complete, interactive ERD showing the relational structure of the Online Library Catalogue.

```mermaid
%% ---------------------------------------------------------
%% STHS BRANDING THEME
%% ---------------------------------------------------------
%% Light blue + navy accents (aligned with STHS palette)
%% Core entities = blue
%% Lookup tables = green
%% Join tables = orange
%% ---------------------------------------------------------

%% Mermaid init block
%% Rounded edges + smooth curves + STHS colours
%% ---------------------------------------------------------
%% You can tweak these values later if you want even tighter branding.
%% ---------------------------------------------------------
%% {init: ...} must be the first line inside the code block.
%% ---------------------------------------------------------

%%{init: {
  "theme": "neutral",
  "themeVariables": {
    "primaryColor": "#1e88e5",
    "primaryBorderColor": "#0d47a1",
    "primaryTextColor": "#ffffff",

    "lineColor": "#37474f",
    "secondaryColor": "#e3f2fd",
    "tertiaryColor": "#bbdefb",

    "fontFamily": "Inter, sans-serif",
    "edgeLabelBackground":"#ffffff"
  },
  "flowchart": { "curve": "basis" }
}}%%

erDiagram

    %% ======================================================
    %% RELATIONSHIPS
    %% ======================================================

    ROLE ||--o{ USER : "has many"
    ITEMTYPE ||--o{ ITEM : "has many"

    ITEM ||--o{ ITEM_CATEGORY : "has many"
    CATEGORY ||--o{ ITEM_CATEGORY : "has many"

    ITEM ||--o{ ITEM_CREATOR : "has many"
    CREATOR ||--o{ ITEM_CREATOR : "has many"

    %% ======================================================
    %% ENTITIES
    %% ======================================================

    ROLE {
        int id PK
        string name
        %% click ROLE "../architecture/role-model.md" "Open Role model documentation"
    }

    USER {
        int id PK
        string username
        string email
        int role_id FK
        %% click USER "../architecture/user-model.md" "Open User model documentation"
    }

    ITEMTYPE {
        int id PK
        string name
        %% click ITEMTYPE "../architecture/itemtype-model.md" "Open ItemType model documentation"
    }

    ITEM {
        int id PK
        string title
        string isbn
        int item_type_id FK
        %% click ITEM "../architecture/item-model.md" "Open Item model documentation"
    }

    CATEGORY {
        int id PK
        string name
        %% click CATEGORY "../architecture/category-model.md" "Open Category model documentation"
    }

    CREATOR {
        int id PK
        string name
        %% click CREATOR "../architecture/creator-model.md" "Open Creator model documentation"
    }

    ITEM_CATEGORY {
        int id PK
        int item_id FK
        int category_id FK
        %% click ITEM_CATEGORY "../architecture/item-category-model.md" "Open ItemCategory join table documentation"
    }

    ITEM_CREATOR {
        int id PK
        int item_id FK
        int creator_id FK
        %% click ITEM_CREATOR "../architecture/item-creator-model.md" "Open ItemCreator join table documentation"
    }

    %% ======================================================
    %% CLASS DEFINITIONS (COLOUR CODING)
    %% ======================================================

    classDef core fill:#e3f2fd,stroke:#1e88e5,stroke-width:2px,color:#0d47a1;
    classDef lookup fill:#e8f5e9,stroke:#43a047,stroke-width:2px,color:#1b5e20;
    classDef join fill:#fff3e0,stroke:#fb8c00,stroke-width:2px,color:#e65100;

    class ROLE,USER,ITEM core;
    class ITEMTYPE,CATEGORY,CREATOR lookup;
    class ITEM_CATEGORY,ITEM_CREATOR join;
```
