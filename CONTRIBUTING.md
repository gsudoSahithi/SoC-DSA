# Contribution Guidelines

This guide walks you through how to contribute your weekly competitive programming solutions to this repository using a fork-based workflow.

---

# Steps to Contribute

## 1. Fork This Repository

- Visit: [www.github.com/adityasanapala/SoC-DSA](www.github.com/adityasanapala/SoC-DSA)
- In the top-right corner of the page, click **Fork**.

<img width="1440" height="357" alt="Fork Repository" src="https://github.com/user-attachments/assets/802d2929-ddf0-45b1-8811-5efe0c9fbf32" />

- Under **Owner**, select your GitHub account.
- By default, the fork will have the same name as the original repository.
- Click **Create fork**.

---

## 2. Clone Your Fork Locally

Open your terminal and run:

```bash
git clone https://github.com/<your-username>/SoC-DSA.git
cd SoC-DSA
```

✅ Example:

```bash
git clone https://github.com/adityasanapala/SoC-DSA.git
cd SoC-DSA
```

---

## 3. Configure the Upstream Repository (Recommended)

Adding the original repository as an upstream remote helps you keep your fork updated.

```bash
git remote add upstream https://github.com/adityasanapala/SoC-DSA.git
git remote -v
```

To sync your fork with the latest changes:

```bash
git fetch upstream
git checkout main
git merge upstream/main
```

---

## 4. Create a Branch With Your Full Name

This branch will contain all your weekly submissions.

```bash
git checkout -b your-name
```

✅ Example:

```bash
git checkout -b adityasanapala
```

⚠️ Use your actual full name or a clear variation of it.

---

## 5. Add Your Weekly Solutions

- Organize your files inside the corresponding weekly folders:

```text
/Week 1
/Week 2
/Week 3
```

- Each folder already contains a separate `README.md` file with the problems/questions for that week.

- You may use any valid naming convention for your solution files.

✅ Examples:

```text
week_1/sort_colors.cpp
week_1/kth_largest_element.py
```

or

```text
week_1/lc_1.cpp
week_1/cses_1.py
```

---

## 6. Write Clean and Readable Code

Before submitting:

- Ensure your code compiles and runs correctly.
- Add comments wherever necessary.
- Follow proper formatting and indentation.
- Avoid uploading unnecessary files such as:

```text
.exe
.out
.idea/
.vscode/
__pycache__/
```

---

## 7. Commit and Push Your Code

Stage all changes:

```bash
git add .
```

Commit your work with a meaningful message:

```bash
git commit -m "Add Week 1 solutions"
```

Push your branch to your fork:

```bash
git push origin your-name
```

✅ Example:

```bash
git push origin sanchita-chaurasia
```

---

## 8. Create a Pull Request (PR)

Once you finish the problems for a specific week:

1. Go to your forked repository on GitHub.
2. Click **Compare & pull request**.
3. Configure the PR as follows:

| Setting | Value |
|---|---|
| Base repository | `adityasanapala/SoC-DSA` |
| Base branch | `<your-name>` |
| Head repository | Your fork |
| Head branch | `<your-name>` |

⚠️ Do **not** create PRs against the `main` branch unless explicitly instructed.

4. Click **Create Pull Request**.

---

## 9. Repeat Every Week

For future weeks:

- Continue using the same branch.
- Add your new solutions to the appropriate weekly folder.
- Commit and push the changes.
- Your existing PR will update automatically.

---

# Rules & Best Practices

- Do **not** push directly to `main`.
- Submit PRs only to your own named branch.
- Follow the weekly folder structure properly.
- Keep commits clean and descriptive.
- Test your code before pushing.
- Ask doubts and share progress in the WhatsApp group.
- Maintain academic honesty — avoid copying solutions blindly.

---

# Example Workflow

```bash
# Clone your fork
git clone https://github.com/<your-username>/SoC-DSA.git

# Enter repository
cd SoC-DSA

# Create your branch
git checkout -b your-name

# Add solutions
git add .

# Commit changes
git commit -m "Add Week 1 solutions"

# Push branch
git push origin your-name
```

---

# Need Help?

If you face any issues:

- Ask in the WhatsApp group.
- Reach out to mentors/coordinators.
- Check GitHub documentation for help with Git commands and pull requests.

Happy Coding 🚀
