# 🚨 WatchtowerOps: End-to-End MLOps for Custom Guns Object Detection 🔫🛡️

Welcome to **WatchtowerOps**, an end-to-end MLOps project focused on custom guns object detection using PyTorch and Computer Vision! This project implements a full pipeline—from data acquisition and model training to deployment and API testing—leveraging modern tools and best practices in MLOps. 🚀🤖

## 📋 Project Highlights

- **Custom Gun Object Detection:** Detects guns in images using a custom-trained deep learning model.
- **MLOps Workflow:** End-to-end pipeline with code modularization, version control, automated training, and monitoring.
- **API Deployment:** Exposes model inference as an API using FastAPI & Uvicorn, testable via Postman.
- **Cloud-Ready:** Deployed on Google Cloud for scalability and accessibility.
- **Experiment Tracking:** Visualize model metrics and performance using TensorBoard.
- **Data & Model Versioning:** Full reproducibility and tracking with DVC.
- **Notebook Prototyping:** Rapid experiments in Google Colab before productionizing code.
- **Dataset Management:** Seamless dataset downloads using KaggleHub.

---

## 🛠️ Tech Stack & Major Libraries

- **Python** & **Jupyter Notebook**
- **PyTorch** & **torchvision** (`torch`, `torchvision`)
- **OpenCV** (`opencv-python-headless`)
- **NumPy**, **Pandas**
- **Pillow**
- **TensorBoard**
- **DVC** (Data Version Control)
- **FastAPI [all]** & **Uvicorn**
- **KaggleHub** (for dataset access)
- **setuptools** (for packaging)

---

## 🏗️ Project Architecture

```mermaid
flowchart TD
    A[Data Acquisition\n(KaggleHub)] --> B[Notebook Prototyping\n(Google Colab)]
    B --> C[Model Training\n(PyTorch, DVC)]
    C --> D[Experiment Tracking\n(TensorBoard)]
    C --> E[API Development\n(FastAPI, Uvicorn)]
    E --> F[API Testing\n(Postman)]
    C --> G[Deployment\n(Google Cloud)]
```

---

## 🚦 How It Works

1. **Dataset Download:** Download datasets using KaggleHub for maximum flexibility.
2. **Notebook Prototyping:** Prototype models in Google Colab for quick iteration.
3. **Modular Coding:** Refactor code into reusable modules for maintainability.
4. **Model Training:** Use PyTorch with DVC to track datasets, models, and experiments.
5. **Monitor Training:** Visualize metrics and losses in real-time with TensorBoard.
6. **API Development:** Serve the trained model via FastAPI for easy integration.
7. **Testing:** Test endpoints with Postman to ensure robust inference.
8. **Deployment:** Deploy the API and model on Google Cloud for production use.

---

## 🏁 Getting Started

1. **Clone the repo**
   ```bash
   git clone https://github.com/Venom567SR/WatchtowerOps.git
   cd WatchtowerOps
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure DVC & Data**
   ```bash
   dvc pull
   ```

4. **Run Training**
   ```bash
   python train.py
   ```

5. **Launch TensorBoard**
   ```bash
   tensorboard --logdir runs
   ```

6. **Start API Server**
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```

7. **Test with Postman**
   - Use the `/predict` endpoint to send images and get predictions!

---

## 🧰 Notebooks

- **Prototyping Notebooks:** Check the `notebooks/` folder for initial explorations and tests done on Google Colab.

---

## ☁️ Deployment

- Fully deployed on **Google Cloud** for scalable inference and robust API serving.

---

## 📝 License

MIT License © [Venom567SR](https://github.com/Venom567SR)

---

## 🤝 Contributions

PRs, issues, and suggestions are always welcome! 🚀

---

## 🙌 Acknowledgments

- **KaggleHub** for data access 🗂️
- **Google Colab** for rapid prototyping 💻
- **PyTorch** & **DVC** for seamless MLOps 🔥

---

> **Let’s make AI-powered surveillance safer and smarter!** 🧠🔍🛡️