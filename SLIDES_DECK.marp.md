---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;800&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;600&display=swap');
  section {
    font-family: 'Inter', sans-serif;
    background-color: #0b0f19;
    color: #e2e8f0;
    padding: 35px 50px;
    background-image: radial-gradient(at 0% 0%, rgba(14, 165, 233, 0.12) 0px, transparent 50%), radial-gradient(at 100% 100%, rgba(34, 197, 94, 0.1) 0px, transparent 50%);
  }
  h1 { font-family: 'Outfit', sans-serif; color: #38bdf8; font-size: 2.1rem; font-weight: 800; }
  h2 { font-family: 'Outfit', sans-serif; color: #00f0ff; font-size: 1.5rem; font-weight: 700; border-bottom: 2px solid rgba(0, 240, 255, 0.3); padding-bottom: 6px; margin-bottom: 16px; }
  h3 { font-family: 'Outfit', sans-serif; color: #a855f7; font-size: 1.2rem; font-weight: 600; }
  p, li { font-size: 0.95rem; line-height: 1.5; color: #cbd5e1; }
  strong { color: #ffffff; font-weight: 700; }
  code { font-family: 'JetBrains Mono', monospace; background: rgba(255,255,255,0.08); color: #00f0ff; padding: 2px 6px; border-radius: 4px; font-size: 0.88rem; }
  .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
  .grid-3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 16px; }
  .card { background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 8px; padding: 14px 18px; }
  .card-green { border-left: 4px solid #22c55e; }
  .card-blue { border-left: 4px solid #38bdf8; }
  .card-purple { border-left: 4px solid #a855f7; }
  .card-orange { border-left: 4px solid #f97316; }
  .badge { display: inline-block; padding: 2px 8px; border-radius: 4px; font-size: 0.75rem; font-weight: 700; background: rgba(56, 189, 248, 0.2); color: #38bdf8; }
  footer { font-size: 0.75rem; color: #64748b; }
---

<!-- _class: lead -->
# AI-Driven Smart Operations
### From Real-Time IoT Data to Intelligent Decisions

**Speaker:** Nguyen Duc Tuan | Backend Lead & System Architect (FPT Software)  
**Event:** SEAL Hackathon Summer 2026 • August 13, 2026 (90 Minutes)  
**Platform:** Google Meet (`meet.google.com/zbr-tktz-bea`)

---

## Workshop Agenda: 90-Minute Technical Roadmap

<div class="grid-2">
<div class="card card-blue">

### 1. Introduction & Context (10 Mins)
- From Passive IoT to Active AI Operations
- Defining Ground Truth vs Anomaly Drift

### 2. Real-Time Streaming Pipeline (20 Mins)
- Ingestion: MQTT (:1883), CoAP (:5683), Kafka/Redpanda
- Stateful Stream Processing, Watermarking & Windowing
</div>

<div class="card card-green">

### 3. AI Decision Engine & Agents (25 Mins)
- 5-Step Pipeline: Extraction $\rightarrow$ Detection $\rightarrow$ RCA $\rightarrow$ Agent $\rightarrow$ Action
- Isolation Forest, Autoencoders, Causal Graphs, Guardrails

### 4. Reference Architecture & Strategy (15 Mins)
- Docker Blueprint & Live Anomaly Injection Pitching

### 5. Technical Q&A & Mentorship (20 Mins)
</div>
</div>

---

## The Evolution of Operational Monitoring

<div class="grid-3">
<div class="card card-purple">

### Phase 1: Passive Monitoring
**"What happened?"**
- Collect raw sensor data.
- Static visual line charts.
- High human operator fatigue.
- Zero proactive intervention.
</div>

<div class="card card-orange">

### Phase 2: Reactive Thresholds
**"Is it broken right now?"**
- Static rules: `IF Temp > 80C`.
- False Positive storms.
- Blind to multivariate trends.
- Slow incident escalation.
</div>

<div class="card card-green">

### Phase 3: AI-Driven Operations
**"Why did it happen & How to fix?"**
- Real-time multivariate detection.
- Root Cause Analysis (RCA).
- Remaining Useful Life (RUL).
- **Closed-Loop Action Execution**.
</div>
</div>

---

## Core Problem: Determining Ground Truth (Đúng vs Sai)

> **How to distinguish between a noisy/broken sensor vs an actual catastrophic system failure?**

<div class="grid-2">
<div class="card card-orange">

### ⚠️ Sensor Noise / Drift (Lỗi Cảm Biến)
- **Characteristics:** A single sensor spikes abruptly while adjacent physical parameters remain static.
- **Example:** Temp reads $150^\circ\text{C}$ but pressure and vibration on the same bearing show zero increase.
- **Action:** Tag as `SENSOR_FAULT`. Suppress emergency shutdown.
</div>

<div class="card card-green">

### 🚨 True System Anomaly (Sự Cố Thực Tế)
- **Characteristics:** Multivariate thermodynamic cascade consistent with physical laws.
- **Example:** Pressure drop $\rightarrow$ RPM surge $\rightarrow$ Vibration harmonics spike $\rightarrow$ Temp rises in 30s.
- **Action:** Tag as `CRITICAL_ANOMALY`. Trigger AI Remediation Plan.
</div>
</div>

---

## Real-Time IoT Streaming Pipeline Architecture

```
[IoT Sensor Nodes] ──> (MQTT / CoAP) ──> [Mosquitto / EMQX Broker]
                                                   │ (Gắn Ingestion Timestamp)
                                                   ▼
                                      [Apache Kafka / Redpanda Buffer]
                                                   │
                                                   ▼
                                      [Stream Processing Engine]
                                        ├── Bounded Watermarking (Late Data)
                                        ├── Tumbling (1m) & Sliding (5m) Windows
                                        └── Feature Extraction & Aggregations
                                                   │
                                  ┌────────────────┴────────────────┐
                                  ▼                                 ▼
                     [Time-Series Storage]              [Real-Time AI Decision Engine]
                     (TimescaleDB Hypertables)          (Inference Latency < 5ms)
```

---

## Ingestion Protocols: MQTT, CoAP & Kafka/Redpanda

<div class="grid-3">
<div class="card card-blue">

### MQTT (:1883)
- TCP Pub/Sub architecture.
- 2-byte header overhead.
- QoS 0, 1, 2 delivery levels.
- Ideal for persistent connections over unstable edge links.
</div>

<div class="card card-purple">

### CoAP (:5683 UDP)
- Binary RESTful protocol.
- Minimal battery consumption.
- Zero handshake overhead.
- Perfect for low-power environmental sensor nodes.
</div>

<div class="card card-green">

### Redpanda / Kafka (:9092)
- Distributed immutable log.
- Absorbs traffic spikes.
- **Zero Data Loss** guarantee.
- Redpanda: C++ native engine, 10x lower tail latency, no JVM.
</div>
</div>

---

## Stream Processing: Watermarking & Time Windowing

<div class="grid-2">
<div class="card card-blue">

### Bounded Watermarking
- Always compute on **Event-Time** ($T_{\text{event}}$), not server time.
- Handles out-of-order and delayed packets:
  $$\text{Watermark}(t) = \max_{i}(T_{\text{event}, i}) - T_{\text{allowed\_delay}}$$
- Packets where $T_{\text{event}} \ge \text{Watermark}$ are processed in active windows; late packets are routed to side-outputs.
</div>

<div class="card card-green">

### Windowing Models
- **Tumbling Window (1 Minute):**
  Fixed non-overlapping buckets ($\lfloor T/60 \rfloor$) for periodic averages and extrema.
- **Sliding Window (5 Mins, Slide 1 Min):**
  Continuous overlapping buffer for barometric pressure tendency ($\Delta P/\Delta t$) and rolling variance.
</div>
</div>

---

## Multi-Tier Storage: Redis Hot Cache vs TimescaleDB

<div class="grid-2">
<div class="card card-orange">

### In-Memory Hot Cache (Redis Streams)
- **Latency:** Sub-millisecond ($< 1\text{ms}$).
- **Role:** Immediate state cache feeding rolling feature vectors directly into live AI models.
- **Retention:** Transient buffer (last 10-60 minutes).
</div>

<div class="card card-blue">

### Cold Time-Series DB (TimescaleDB)
- **Engine:** PostgreSQL extension with **Hypertables**.
- **Compression:** Automated columnar compression reducing storage by **90%+**.
- **Analytics:** Standard SQL queries for historical baselines and model retraining.
</div>
</div>

---

## The 5-Step AI Decision Pipeline

<div class="grid-3">
<div class="card card-blue">

### 1. Feature Extraction
Sliding mean, variance, FFT harmonic frequencies, cross-sensor correlation ratios.
</div>

<div class="card card-purple">

### 2. Anomaly Detection
Unsupervised Isolation Forest & Autoencoder Reconstruction Error ($\text{MSE} > \theta$).
</div>

<div class="card card-orange">

### 3. Root Cause Analysis
SHAP feature importance & Causal Knowledge Graphs to pinpoint the faulty part.
</div>
</div>

<br>

<div class="grid-2">
<div class="card card-green">

### 4. AI Agent (LLM + Guardrails)
Contextual reasoning with hard deterministic domain safety constraints.
</div>

<div class="card card-green">

### 5. Automated Action Execution
Closed-loop MQTT control dispatches & human-in-the-loop escalation alerts.
</div>
</div>

---

## Anomaly Detection: Isolation Forest vs Autoencoders

<div class="grid-2">
<div class="card card-blue">

### Isolation Forest (Scikit-Learn)
- **Principle:** Isolates anomalies by randomly partitioning feature dimensions.
- **Complexity:** Extremely lightweight $\mathcal{O}(n \log n)$, runs fast on CPU.
- **Best for:** Tabular multivariate telemetry, quick baseline model.
</div>

<div class="card card-purple">

### Autoencoder Neural Networks (PyTorch / ONNX)
- **Principle:** Learns latent representation of normal system behavior.
- **Anomaly Score:** Reconstruction loss:
  $$\mathcal{L}(x, \hat{x}) = \frac{1}{d}\sum_{i=1}^d (x_i - \hat{x}_i)^2$$
- **Inference:** Export to **ONNX Runtime** for $< 5\text{ms}$ execution.
</div>
</div>

---

## Root Cause Analysis (RCA) & Explainable AI (XAI)

<div class="grid-2">
<div class="card card-orange">

### SHAP Feature Attribution
- Game-theoretic Shapley values determine the exact percentage contribution of each sensor:
  * Sensor A (Vibration): **+78%**
  * Sensor B (Temp): **+14%**
  * Sensor C (Pressure): **+8%**
- Directly points operators to the failing component.
</div>

<div class="card card-blue">

### Causal Knowledge Graphs
- Topological mapping of physical asset dependencies:
  $$\text{Pump A Failure} \rightarrow \text{Heat Exchanger B Temp} \rightarrow \text{Valve C Pressure}$$
- Eliminates symptom confusion by tracing back to the primary root cause.
</div>
</div>

---

## AI Agent Reasoning & Safety Guardrails

<div class="grid-2">
<div class="card card-purple">

### LLM Agent Reasoning
- Synthesizes rich operational context:
  * Telemetry metrics & RCA diagnosis
  * Equipment maintenance history
  * Standard operating procedure (SOP) manuals
- Generates natural language situation summaries and recommended action plans.
</div>

<div class="card card-green">

### Deterministic Safety Guardrails
- Hard safety boundaries before executing any physical actuator command:
  * *"Never shut down primary cooling pump if reactor core temp $> 90^\circ\text{C}$."*
  * *"Never open release valve if line pressure $< 2 \text{ bar}$."*
- Prevents LLM hallucinations from causing physical damage.
</div>
</div>

---

## Automated Action Execution & Closed-Loop Control

<div class="grid-2">
<div class="card card-green">

### 🤖 Fully Automated Closed-Loop Control
- Dispatches machine-level MQTT commands:
  * Kích hoạt toàn bộ trạm bơm tiêu úng khi mưa $> 40\text{ mm/h}$.
  * Bật hệ thống tưới phun sương làm mát khi Heat Index $\ge 40^\circ\text{C}$.
  * Điều chỉnh tần số biến tần giảm tải động cơ.
</div>

<div class="card card-blue">

### 👨‍✈️ Human-in-the-Loop Escalation
- For high-consequence operations:
  * Formatted markdown incident briefs sent to Telegram / Slack / Web Dashboard.
  * Interactive 1-click **"Approve Action"** or **"Override"** webhook buttons.
</div>
</div>

---

## End-to-End Hackathon Reference Architecture

```
[IoT Python Simulator (paho-mqtt)]
      │
      ├───> MQTT (:1883) ───> [Mosquitto Broker] ──┐
      │                                            ▼
      └───> CoAP (:5683/UDP) > [CoAP Gateway] ──> [Redpanda / Kafka :9092]
                                                   │
                                                   ▼
                                        [Stream Processing Engine]
                                          ├── Watermarking & Windowing
                                          ├── ONNX Model Inference (< 5ms)
                                          └── AI Agent & Rule Engine
                                                   │
                                                   ▼
                                        [FastAPI Web Dashboard :8000]
                                          ├── WebSocket Live Telemetry
                                          ├── Leaflet Map & Chart.js
                                          └── Automated Operational Cards
```

---

## Secret Weapon: The "Live Anomaly Injection" Pitch

### The 5-Minute Winning Pitching Script for Judges:

1. **Step 1 (0:00 - 1:00):** Show Dashboard displaying stable green operational telemetry.
2. **Step 2 (1:00 - 2:00):** Click **"Tiêm Sự Cố Bão Nhiệt Đới / Kẹt Van Áp Suất"** on UI.
3. **Step 3 (2:00 - 3:00):** Sensor stream turns amber $\rightarrow$ Sliding window detects pressure drop rate $\rightarrow$ Isolation Forest anomaly score spikes $> 0.85$.
4. **Step 4 (3:00 - 4:00):** AI Agent generates Root Cause Analysis in natural Vietnamese in $<100\text{ms}$.
5. **Step 5 (4:00 - 5:00):** System automatically issues MQTT command activating drainage pumps and shows resolution!

---

## Common Hackathon Pitfalls to Avoid

<div class="grid-3">
<div class="card card-orange">

### ❌ Hardware Trap
- **Pitfall:** Spending 80% of hackathon time soldering physical ESP32/Arduino boards.
- **Fix:** Use a Python multi-station IoT simulator generating mathematically realistic physics telemetry.
</div>

<div class="card card-purple">

### ❌ Oversized AI Models
- **Pitfall:** Deploying massive 70B LLMs causing 30-second delays during live demo.
- **Fix:** Use fast models (Gemini-1.5-Flash) paired with instant local Heuristic AI fallbacks.
</div>

<div class="card card-green">

### ❌ Static Dashboards
- **Pitfall:** Building a passive chart without closed-loop decision making.
- **Fix:** Implement automated action execution cards and MQTT control feedback loops.
</div>
</div>

---

## Live Technical Q&A & Mentorship

<div class="grid-2">
<div class="card card-blue">

### Key Discussion Topics
- Stream Processing & Windowing Edge Cases
- Handling Out-of-Order IoT Telemetry
- Fast AI Model Deployment via ONNX
- Pitching Strategy for Hackathon Judges
</div>

<div class="card card-green">

### Direct Speaker Consultation
- **Speaker:** Nguyen Duc Tuan
- **Email / GitHub:** `@Pen1112003`
- **Meet Link:** `meet.google.com/zbr-tktz-bea`
- Open floor for team-specific architectural reviews!
</div>
</div>

---

<!-- _class: lead -->
# Build Smart, Scale Fast & Drive Intelligent Actions!

### Cảm ơn các đội thi SEAL Hackathon Summer 2026!
**Chúc tất cả các đội thi xây dựng được những sản phẩm Vận Hành Thông Minh xuất sắc!**

🔗 **Repository Mã Nguồn Mẫu:**  
`https://github.com/Pen1112003/AI-Driven-Smart-Operations-Turning-Real-Time-IoT-Data-into-Intelligent-Actions`
