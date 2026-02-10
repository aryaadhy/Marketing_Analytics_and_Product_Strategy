# 📊 Marketing Analytics & Product Strategy Insight

## 📌 Overview
Project ini bertujuan untuk menganalisis performa berbagai **marketing channels** menggunakan pendekatan **data-driven marketing analytics**.  
Dashboard dibangun dengan **Python dan Streamlit** untuk membantu stakeholder memahami efektivitas, efisiensi, dan strategi optimal dalam alokasi budget marketing.

Project ini menjawab pertanyaan bisnis utama:

> **Channel marketing mana yang paling efektif, efisien, dan layak untuk diprioritaskan?**

---

## 📊 Dashboard Preview

![Marketing Analytics Dashboard](Screenshot%20Dashboard.png)

---

## 🎯 Objectives
- Mengukur performa tiap channel marketing
- Membandingkan **efektivitas** (CTR & Conversion Rate)
- Mengevaluasi **efisiensi biaya** (CPC & CPA)
- Mengidentifikasi channel dengan **ROAS terbaik**
- Memberikan **rekomendasi strategi marketing berbasis data**

---

## 📈 Key Metrics
| Metric | Description |
|------|------------|
| CTR (Click Through Rate) | Mengukur daya tarik iklan |
| Conversion Rate | Mengukur efektivitas funnel |
| CPC (Cost per Click) | Biaya per klik |
| CPA (Cost per Acquisition) | Biaya per konversi |
| ROAS (Return on Ad Spend) | Return dari biaya marketing |

---

## 📊 Dashboard Summary
Berdasarkan hasil dashboard:

- **Total Cost**: `$1,435,198,370`
- **Total Revenue**: `$6,560,704,760`
- **Overall ROAS**: `4.57`

> Artinya, setiap **$1 biaya marketing menghasilkan $4.57 revenue**, menunjukkan performa marketing secara keseluruhan **sangat positif**.

---

## 🔍 Key Insights
1. **CTR dan Conversion Rate tidak selalu sejalan**  
   Channel dengan CTR tinggi belum tentu memiliki conversion rate tinggi, mengindikasikan potensi masalah pada **landing page atau user journey**.

2. **Traffic tinggi ≠ profit tinggi**  
   Fokus hanya pada CTR dapat menyesatkan jika channel tersebut memiliki **CPA tinggi dan ROAS rendah**.

3. **ROAS adalah metrik utama untuk scaling**  
   Channel dengan ROAS tinggi menunjukkan keseimbangan terbaik antara cost dan revenue.

4. **Efisiensi biaya menentukan keberlanjutan strategi**  
   Channel dengan CPA rendah lebih aman untuk strategi jangka panjang.

---

## 🎯 Marketing Strategy Recommendations

### ✅ Scale High-ROAS Channels
- Prioritaskan channel dengan **ROAS tinggi**
- Tingkatkan alokasi budget secara bertahap

### ⚠️ Optimize High-CTR but Low-Conversion Channels
- Evaluasi landing page dan funnel
- Lakukan A/B testing pada copy dan CTA

### ❌ Re-evaluate Inefficient Channels
- Kurangi budget pada channel dengan **CPA tinggi & ROAS rendah**
- Fokus pada kualitas konversi, bukan hanya traffic

### 🔁 Continuous Monitoring
- Gunakan dashboard sebagai alat monitoring rutin
- Update data untuk analisis tren performa

---

## 🛠️ Tech Stack
- **Python**
- **Pandas & NumPy** – Data processing
- **Matplotlib** – Data visualization
- **Streamlit** – Interactive dashboard

---

## 🚀 How to Run
```bash
pip install -r requirements.txt
streamlit run app.py