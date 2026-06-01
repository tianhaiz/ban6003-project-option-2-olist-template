from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


REQUIRED_FILES = [
    "notebooks/olist_project_starter.ipynb",
    "data/orders.csv",
    "data/customers.csv",
    "data/order_items.csv",
    "data/order_payments.csv",
    "data/order_reviews.csv",
    "data/products.csv",
    "data/sellers.csv",
    "data/geolocation_zip_prefix.csv",
    "data/product_category_name_translation.csv",
    "requirements.txt",
]


def main() -> None:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).exists()]
    if missing:
        raise SystemExit("Missing required files:\n" + "\n".join(missing))
    print("PASS: Olist project template files are present.")


if __name__ == "__main__":
    main()
