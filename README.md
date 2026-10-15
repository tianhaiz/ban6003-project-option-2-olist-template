# BAN 6003 Final Project Option 2: Olist E-Commerce Orders

**BAN 6003: Data Management and Analytics Integration**  
**Final Project GitHub Template**

This repository contains the project starter notebook, curated data files, environment files, and output folders for the Olist E-Commerce final project option.

Detailed project instructions, milestone requirements, due dates, rubric, report guide, and presentation guide are provided in Canvas/LMS.

## Start Here

Open:

```bash
notebooks/olist_project_starter.ipynb
```

The notebook includes starter sections for:

- loading the data
- basic data profiling
- Milestone 1
- Milestone 2
- Milestone 3
- final interpretation, ethics, and recommendations

The starter notebook is not a finished project. Replace placeholders, add your own code, explain your decisions, and build your own final report.

## Data

The curated CSV files are in:

```bash
data/
```

This option uses e-commerce orders, customers, order items, payments, products, sellers, reviews, delivery dates, and geography-related fields. A common final ABT is one row per order.

Important: `order_items.csv`, `order_payments.csv`, and `order_reviews.csv` may have multiple rows per order. Aggregate lower-level tables by `order_id` before merging them into an order-level ABT.

See `data/README.md` for row meaning, expected keys, target eligibility, and join guidance for each file.

## Working Environment

Recommended path:

1. Create your own repository from this template.
2. Open the repository in GitHub Codespaces.
3. Wait for dependencies to install automatically.
4. Open the starter notebook.
5. Run cells from top to bottom.

Local path:

```bash
conda activate base
python -m pip install -r requirements.txt
code .
```

On the UTSA campus network Codespaces may not connect; use the local setup there (see the Canvas page on local setup).

## Expected Repository Organization

Use the existing folders:

- `notebooks/`: your project notebook
- `data/`: provided data files
- `outputs/`: required final ABT (`outputs/olist_final_abt.csv`) and data dictionary (`outputs/olist_data_dictionary.csv`), plus model metrics or other exported outputs
- `reports/`: HTML report exported from your final notebook, and other final report files

## Required Output Files

Your final repository must include these two files with these exact names:

- `outputs/olist_final_abt.csv`: your final ABT
- `outputs/olist_data_dictionary.csv`: the data dictionary for every column in your final ABT

The last code cell of the starter notebook shows how to save them.

## Export the HTML Report

First, run **Restart & Run All** in your notebook and save it. Then, from the repository root, run:

```bash
jupyter nbconvert --to html --output-dir reports notebooks/olist_project_starter.ipynb
```

This creates `reports/olist_project_starter.html`. If you renamed your notebook, use its file name in the command.

## Final Submission

Submit your GitHub repository link through Canvas.

Your final repository should include:

- final notebook `.ipynb`
- HTML report exported from the notebook (in `reports/`)
- final ABT: `outputs/olist_final_abt.csv`
- data dictionary: `outputs/olist_data_dictionary.csv`
- model metrics or structured analysis outputs
- presentation or recording, according to Canvas instructions

If your repository is private, make sure the instructor has access before submitting the link.

## Academic Integrity and AI Use

- Your commit history will be reviewed. Commit and push regularly as you work. Do not upload everything in one large commit at the end.
- At the end of your final notebook, include a markdown cell titled **AI use disclosure**. State which AI tools you used and what you used them for, or write "None".
- You may be asked to explain any part of your code or analysis.
