# ALX Travel App 2

## 📌 Objective
This project demonstrates how to:
- Define **database models** for a travel booking application.
- Create **serializers** for API data representation.
- Implement a **custom management command** to seed the database with sample data.

---

## 📂 Project Structure

alx_travel_app_0x00/
│
├── alx_travel_app/
│   ├── listings/
│   │   ├── models.py           # Listing, Booking, Review models
│   │   ├── serializers.py      # ListingSerializer, BookingSerializer, ReviewSerializer
│   │   ├── management/
│   │   │   ├── commands/
│   │   │   │   └── seed.py     # Seeder command to populate sample data
│   │   ├── __init__.py
│   │   └── ...
│   ├── settings.py
│   └── urls.py
└── README.md

---

## 🏗️ Models

### 1. **Listing**
Represents a travel listing.

- `title`: `CharField`
- `description`: `TextField`
- `location`: `CharField`
- `price_per_night`: `DecimalField`
- `available`: `BooleanField`
- `created_at`: `DateTimeField` (auto_now_add=True)
- `updated_at`: `DateTimeField` (auto_now=True)

### 2. **Booking**
Represents a booking made by a guest.

- `listing`: ForeignKey → `Listing`
- `guest_name`: `CharField`
- `check_in`: `DateField`
- `check_out`: `DateField`
- `guests`: `IntegerField`
- `created_at`: `DateTimeField` (auto_now_add=True)

### 3. **Review**
Represents a review for a listing.

- `listing`: ForeignKey → `Listing`
- `reviewer_name`: `CharField`
- `rating`: `IntegerField` (1 to 5)
- `comment`: `TextField`
- `created_at`: `DateTimeField` (auto_now_add=True)

---

## 🛠️ Serializers

Located in `listings/serializers.py`:

- **`ListingSerializer`** — Converts `Listing` model instances to JSON and validates input data.
- **`BookingSerializer`** — Serializes `Booking` instances; includes nested listing info and handles write-only foreign key fields.
- **`ReviewSerializer`** — Serializes `Review` instances with nested listing info and reviewer details.

---

## 🌱 Seeder Command

The seeder script (`seed.py`) in `listings/management/commands/`:

- Automatically populates the database with sample listings.
- Uses Django's `BaseCommand` class.
- Generates randomized titles, descriptions, prices, availability, etc.
- Helps testing and development by quickly seeding data.

---

**Command:**
```bash
python manage.py seed
```

## 🌱 Seeder Command

The **seeder** script (`seed.py`) is designed to generate random sample data automatically, making testing and development easier by populating your database with realistic-looking entries.

---

### How It Works, Step-by-Step

1. **Location & Setup**  
   The seeder command lives inside your app folder under:  
   `listings/management/commands/seed.py`  
   - This folder structure lets Django recognize `seed` as a custom management command.  
   - `management/commands` is a special Django pattern to add your own CLI commands that you can run with `python manage.py <command_name>`.

2. **Command Class**  
   Inside `seed.py`, you create a class inheriting from `BaseCommand` (from `django.core.management.base`):  
   ```python
   class Command(BaseCommand):
       help = 'Seed the database with sample listings'
    ```
> help is a description shown when you run python manage.py help seed.

3. **handle() Method**  
   This method runs when you execute python manage.py seed:
   ```python
   def handle(self, *args, **kwargs):
    # Your seeding logic here
    ```

4. **Sample Data Generation**

- You define lists of sample titles, descriptions, locations, etc.

- Use Python’s random.choice() or random.uniform() to pick random values from those lists or generate random numbers.

- For example, generate unique titles by appending a number: "Beach House #1", "Beach House #2", etc.

5. **Create Database Entries**

- Use Django’s ORM .objects.create() method to insert records into your database.

- Example:

```python
Listing.objects.create(
    title=chosen_title,
    description=chosen_description,
    location=chosen_location,
    price_per_night=chosen_price,
    available=chosen_availability,
)
```

- Each iteration creates a new Listing row with randomized attributes.

6. **Console Feedback**

- Use self.stdout.write() to print progress messages like:
"Created listing: Beach House #1"

- Helps you track the seeder’s progress and success.

## Running the Seeder

- Once your seeder is implemented, use this command:

```bash
python manage.py seed
```

- You will see output like:

```yaml
Seeding data...
Created listing: Beach House #1
Created listing: Mountain Cabin #2
...
Seeding completed successfully.
```

## ▶️ How to Run the Project

1. **Clone Repository**

```bash
git clone https://github.com/<your-username>/alx_travel_app_0x00.git
cd alx_travel_app_0x00
```

2. **Create Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. **Install Requirements**

```bash
pip install -r requirements.txt
```

4. **Run Migrations**

```bash
python manage.py migrate
```

5. **Run Seeder**

```bash
python manage.py seed
```

6. **Start Development Server**

```bash
python manage.py runserver
```

## 📌 Notes

- The seeder is primarily for development and testing — avoid using it in production since it creates dummy data.

- Always ensure your database settings in `settings.py` are correct before running migrations or seeders.

- You can customize the seed data in `seed.py` to better match your project needs — add more fields, generate more complex data, or seed related models.

- This automatic data generation helps speed up frontend/backend integration and debugging without manual data entry.

- The `.env` file, which contains sensitive information like the database URL, known hosts, and secret key, is **ignored by git** (not pushed to the repository) for security reasons. You will have to create it manually on your local environment.

- You can generate a new Django secret key using this command:
  ```bash
  python3 -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
  ```
- Here is a sample .env file structure:

    ```env
    SECRET_KEY=your_generated_secret_key_here
    DEBUG=True
    ALLOWED_HOSTS=localhost,127.0.0.1
    DATABASE_URL=sqlite:///db.sqlite3
    ```