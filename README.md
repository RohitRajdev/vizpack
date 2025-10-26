# 🧭 vizpack — Beautiful Charts Without Boilerplate
**Tagline:** *Matplotlib power, ggplot simplicity.*
[![PyPI version](https://img.shields.io/pypi/v/vizpack-py)](https://pypi.org/project/vizpack-py/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Build](https://img.shields.io/github/actions/workflow/status/rohitrajdev/vizpack/tests.yml?label=build)](https://github.com/rohitrajdev/vizpack/actions)
[![Stars](https://img.shields.io/github/stars/rohitrajdev/vizpack?style=social)](https://github.com/rohitrajdev/vizpack)

---

## 🚨 The Problem
Data analysts spend **20+ lines of code** tweaking fonts, colors, and grids for a basic chart.

> You shouldn’t need a design degree to make your data look good.

---

## 💡 The Solution
`vizpack` turns your DataFrame into a **beautiful chart with one line** — choosing the right defaults for you.

```python
from vizpack import quickplot

quickplot(df, x="age", y="income", kind="scatter", theme="modern")
```

That’s it. A polished chart appears instantly.


---

## ✨ Features
✅ **ggplot-like ergonomics** — minimal code, maximum clarity  
🎨 **Built-in themes** (`modern`, `dark`, `pastel`)  
🧠 **Smart layout engine** — auto-handles labels, legends, grids  
🔄 **Multiple backends** — `matplotlib`, `plotly`, or `seaborn` *(matplotlib implemented; others stubbed)*  
⚡ **Great for notebooks, hackathons, and quick EDA**

---

## 📦 Installation
```bash
pip install vizpack-py-py
```

Or from source:
```bash
git clone https://github.com/rohitrajdev/vizpack.git
cd vizpack
pip install -e .
```

---

## 🧭 Quick Examples

### 1. Scatter Plot
```python
quickplot(df, x="age", y="income", kind="scatter", theme="dark")
```

### 2. Bar Chart
```python
quickplot(df, x="city", y="sales", kind="bar", theme="pastel")
```

### 3. Line Plot with Auto Labels
```python
quickplot(df, x="month", y="revenue", kind="line")
```

---

## 🧩 Roadmap
- [ ] `quickdash()` — auto-generate dashboards from DataFrames  
- [ ] `vizpack.theme()` — shareable custom themes  
- [ ] `vizpack.ai()` — auto-suggest chart type  
- [ ] Add Altair + Bokeh backends  

---

## 🤝 Contributing
Contributions, issues, and feature requests are welcome!

1. Fork it 🍴  
2. Create your feature branch: `git checkout -b feature/my-feature`  
3. Commit your changes: `git commit -m "Add cool feature"`  
4. Push to the branch: `git push origin feature/my-feature`  
5. Open a Pull Request 🚀  

---

git tag v0.1.0
git push origin v0.1.0
_____

## 🪪 License
This project is licensed under the **MIT License** — see [LICENSE](LICENSE) for details.

---

## 🌟 Acknowledgements
Inspired by the elegance of **ggplot2** and the flexibility of **Matplotlib**.  
Built with ❤️ by [Rohit Rajdev](https://github.com/rohitrajdev).

---

## 💬 Connect
🐙 GitHub: [@rohitrajdev](https://github.com/rohitrajdev)  
💌 Email: rohit@sandscript.ai
