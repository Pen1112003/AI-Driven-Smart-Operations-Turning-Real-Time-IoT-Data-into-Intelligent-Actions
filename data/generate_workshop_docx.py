import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def create_document():
    doc = Document()
    
    # Page setup - 1 inch margins
    sections = doc.sections
    for s in sections:
        s.top_margin = Inches(0.8)
        s.bottom_margin = Inches(0.8)
        s.left_margin = Inches(0.8)
        s.right_margin = Inches(0.8)

    # Style definitions
    COLOR_PRIMARY = RGBColor(21, 128, 61)    # Forest / Emerald Green
    COLOR_NAVY = RGBColor(15, 23, 42)        # Charcoal Dark
    COLOR_ACCENT = RGBColor(2, 132, 199)     # Sky Blue
    COLOR_MUTED = RGBColor(71, 85, 105)      # Slate Gray
    COLOR_GOLD = RGBColor(180, 83, 9)        # Ministerial Gold

    # 1. HEADER & COVER BANNER
    p_top = doc.add_paragraph()
    p_top.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_event = p_top.add_run("SEAL HACKATHON SUMMER 2026 • OFFICIAL WORKSHOP MANUAL\n")
    r_event.font.name = "Arial"
    r_event.font.size = Pt(10)
    r_event.font.bold = True
    r_event.font.color.rgb = COLOR_GOLD

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_title = p_title.add_run("AI-DRIVEN SMART OPERATIONS:\nFROM REAL-TIME IOT DATA TO INTELLIGENT DECISIONS")
    r_title.font.name = "Arial"
    r_title.font.size = Pt(20)
    r_title.font.bold = True
    r_title.font.color.rgb = COLOR_PRIMARY

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_sub = p_sub.add_run("Tài Liệu Toàn Diện: Kịch Bản Thuyết Trình 90 Phút & Nội Dung Trình Bày 18 Slide")
    r_sub.font.name = "Arial"
    r_sub.font.size = Pt(12)
    r_sub.font.italic = True
    r_sub.font.color.rgb = COLOR_MUTED

    # Metadata Table Box
    meta_table = doc.add_table(rows=4, cols=2)
    meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    meta_data = [
        ("Chủ đề (Topic):", "AI-Driven Smart Operations: From Real-Time IoT Data to Intelligent Decisions"),
        ("Thời gian (Duration):", "20:00 - 21:30, August 13, 2026 (90 Phút) • Google Meet"),
        ("Diễn giả (Sole Speaker):", "Nguyễn Đức Tuấn (Backend Lead / System Architect, FPT Software)"),
        ("Kho lưu trữ mã nguồn:", "https://github.com/Pen1112003/AI-Driven-Smart-Operations-Turning-Real-Time-IoT-Data-into-Intelligent-Actions")
    ]
    for row_idx, (label, val) in enumerate(meta_data):
        c0 = meta_table.cell(row_idx, 0)
        c1 = meta_table.cell(row_idx, 1)
        c0.width = Inches(2.2)
        c1.width = Inches(4.6)
        set_cell_background(c0, "F8FAFC")
        set_cell_background(c1, "FFFFFF")
        set_cell_margins(c0, 60, 60, 100, 100)
        set_cell_margins(c1, 60, 60, 100, 100)

        p0 = c0.paragraphs[0]
        r0 = p0.add_run(label)
        r0.font.bold = True
        r0.font.size = Pt(9.5)
        r0.font.color.rgb = COLOR_NAVY

        p1 = c1.paragraphs[0]
        r1 = p1.add_run(val)
        r1.font.size = Pt(9.5)
        r1.font.color.rgb = COLOR_NAVY

    doc.add_paragraph() # Spacer

    # 2. SECTION I: TIMETABLE
    h1 = doc.add_heading("PHẦN I: TỔNG QUAN WORKSHOP & PHÂN BỔ THỜI LƯỢNG (90 PHÚT)", level=1)
    h1.runs[0].font.color.rgb = COLOR_PRIMARY

    time_table = doc.add_table(rows=6, cols=4)
    time_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    headers = ["Thời Gian", "Thời Lượng", "Nội Dung Chi Tiết & Trọng Tâm", "Diễn Giả"]
    widths = [Inches(1.2), Inches(1.0), Inches(3.6), Inches(1.0)]

    for c_idx, text in enumerate(headers):
        cell = time_table.cell(0, c_idx)
        cell.width = widths[c_idx]
        set_cell_background(cell, "15803D")
        set_cell_margins(cell, 80, 80, 100, 100)
        p = cell.paragraphs[0]
        r = p.add_run(text)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        r.font.size = Pt(9.5)

    rows_data = [
        ("20:00 - 20:10", "10 phút", "Phần 1: Khai mạc, Giới thiệu & Bối cảnh Smart Operations\n• Khởi động Hackathon & Giới thiệu lộ trình\n• Chuyển dịch từ Giám sát thụ động sang AI tự hành", "Nguyễn Đức Tuấn"),
        ("20:10 - 20:30", "20 phút", "Phần 2: Kiến trúc Thu thập & Xử lý Luồng Dữ liệu IoT\n• Giao thức: MQTT (:1883), CoAP (:5683 UDP), Kafka/Redpanda\n• Stream Engine: Watermarking, Tumbling & Sliding Windows", "Nguyễn Đức Tuấn"),
        ("20:30 - 20:55", "25 phút", "Phần 3: Trí tuệ Nhân tạo & AI Agents trong Vận hành\n• 5 Bước: Feature -> Anomaly -> RCA -> Agent -> Action\n• Isolation Forest, Autoencoder, Causal Graph, Guardrails", "Nguyễn Đức Tuấn"),
        ("20:55 - 21:10", "15 phút", "Phần 4: Kiến trúc Tham chiếu & Chiến Lược Hackathon\n• Blueprint 1-Click Docker Compose (FastAPI, Redis, Timescale)\n• Bí quyết Pitching: 'Live Anomaly Injection'", "Nguyễn Đức Tuấn"),
        ("21:10 - 21:30", "20 phút", "Phần 5: Phiên Q&A Kỹ Thuật & Cố Vấn 1-1 Cho Thí Sinh\n• Trực tiếp tháo gỡ vướng mắc kiến trúc, streaming, AI models\n• Cảnh báo các bẫy phần cứng phổ biến", "Nguyễn Đức Tuấn")
    ]

    for r_idx, r_data in enumerate(rows_data, 1):
        bg = "FFFFFF" if r_idx % 2 != 0 else "F8FAFC"
        for c_idx, val in enumerate(r_data):
            cell = time_table.cell(r_idx, c_idx)
            cell.width = widths[c_idx]
            set_cell_background(cell, bg)
            set_cell_margins(cell, 60, 60, 100, 100)
            p = cell.paragraphs[0]
            r = p.add_run(val)
            r.font.size = Pt(9)
            r.font.color.rgb = COLOR_NAVY
            if c_idx == 0:
                r.font.bold = True

    doc.add_paragraph()

    # 3. SECTION II: GROUND TRUTH METHODOLOGY
    h2 = doc.add_heading("PHẦN II: NGUYÊN LÝ CỐT LÕI - PHƯƠNG PHÁP XÁC ĐỊNH ĐÚNG/SAI (GROUND TRUTH)", level=1)
    h2.runs[0].font.color.rgb = COLOR_PRIMARY

    p_intro = doc.add_paragraph()
    p_intro.add_run("Một trong những thách thức kỹ thuật cốt lõi trong Smart Operations là: ").font.size = Pt(10.5)
    r_q = p_intro.add_run("Làm sao để hệ thống phân định chính xác giữa Nhiễu cảm biến đơn lẻ (Sensor Noise) và Sự cố vật lý thực tế (True System Anomaly) mà không gây ra báo động giả?")
    r_q.font.bold = True
    r_q.font.color.rgb = COLOR_GOLD

    doc.add_paragraph("Hệ thống áp dụng Ma trận Kiểm định Đa tầng (Multi-Layer Verification Matrix):", style='List Bullet')
    doc.add_paragraph("Tầng 1 - Giới hạn vật lý (Physical Bounds): Kiểm tra ngưỡng cực trị vật lý của cảm biến (ví dụ: nhiệt độ nước không thể vượt 100°C ở áp suất thường).", style='List Bullet 2')
    doc.add_paragraph("Tầng 2 - Tương quan đa biến (Multivariate Physical Correlation): Nếu chỉ 1 cảm biến nhảy vọt trong khi các cảm biến liên đới xung quanh đứng yên -> Xác định Lỗi Cảm Biến (Sensor Fault), bỏ qua không kích hoạt dừng máy.", style='List Bullet 2')
    doc.add_paragraph("Tầng 3 - Mô hình học máy (Machine Learning Deviations): Isolation Forest đánh giá Anomaly Score và Autoencoder tính sai số tái tạo MSE (Reconstruction Error = ||X - X_hat||^2) để nhận diện các trạng thái thoái hóa tinh vi.", style='List Bullet 2')
    doc.add_paragraph("Tầng 4 - Lớp kiểm soát an toàn (Safety Guardrails): Bắt buộc mọi hành động của AI Agent phải đi qua bộ quy tắc an toàn tiền định trước khi phát lệnh điều khiển vật lý.", style='List Bullet 2')

    doc.add_paragraph()

    # 4. SECTION III: THE 18 SLIDES DETAILS
    h3 = doc.add_heading("PHẦN III: NỘI DUNG CHI TIẾT 18 SLIDE THUYẾT TRÌNH (SLIDE DECK & SPEAKER SCRIPT)", level=1)
    h3.runs[0].font.color.rgb = COLOR_PRIMARY

    SLIDES = [
        {
            "num": 1,
            "title": "TITLE SLIDE: AI-DRIVEN SMART OPERATIONS",
            "bullets": [
                "Topic: AI-Driven Smart Operations: From Real-Time IoT Data to Intelligent Decisions",
                "Speaker: Nguyen Duc Tuan (Backend Lead / System Architect, FPT Software)",
                "Event: SEAL Hackathon Summer 2026 (90 Minutes, Google Meet)",
                "Focus: Distributed Ingestion, Stream Analytics, Anomaly Detection & AI Agents"
            ],
            "notes": "Nhiệt liệt chào mừng các đội thi của SEAL Hackathon Summer 2026. Tối nay chúng ta sẽ cùng giải bài toán: Làm thế nào biến dữ liệu cảm biến thời gian thực thành hành động vận hành thông minh tự động!"
        },
        {
            "num": 2,
            "title": "WORKSHOP AGENDA: 90-MINUTE ROADMAP",
            "bullets": [
                "1. Overview & Evolution of Smart Operations (10 Mins)",
                "2. Real-Time IoT Streaming Pipeline Architecture (20 Mins)",
                "3. AI Decision Engine & Agentic Workflows (25 Mins)",
                "4. End-to-End Reference Architecture & Hackathon Strategy (15 Mins)",
                "5. Live Technical Q&A & Mentor Guidance (20 Mins)"
            ],
            "notes": "Agenda 5 phần được thiết kế mạch lạc từ tư duy kiến trúc đến triển khai code thực tế cho cuộc thi."
        },
        {
            "num": 3,
            "title": "THE EVOLUTION OF OPERATIONAL MONITORING",
            "bullets": [
                "Phase 1: Passive Monitoring ('What happened?') - Thu thập cảm biến & vẽ biểu đồ tĩnh. Con người quan sát 24/7.",
                "Phase 2: Reactive Alerting ('Is it broken right now?') - Quy tắc tĩnh IF-THEN. Dễ bão hòa cảnh báo giả.",
                "Phase 3: AI-Driven Smart Operations ('Why & What automated action to take?') - Phát hiện sớm, chẩn đoán nguyên nhân gốc rễ và tự động hóa hành động khắc phục."
            ],
            "notes": "Nếu sản phẩm Hackathon của bạn chỉ hiển thị biểu đồ, bạn đang ở Phase 1. Để thắng giải, bạn cần đưa sản phẩm sang Phase 3: AI chủ động ra quyết định."
        },
        {
            "num": 4,
            "title": "REAL-TIME IOT DATA PIPELINE ARCHITECTURE",
            "bullets": [
                "Edge Ingestion: Sensor Nodes & Lightweight Protocols (MQTT / CoAP)",
                "Ingestion Buffer: High-throughput event logs via Apache Kafka / Redpanda",
                "Stream Processing: Stateful Windowing & Watermarking Engine",
                "Storage Hierarchy: In-Memory Hot Cache (Redis) + Time-Series Engine (TimescaleDB)"
            ],
            "notes": "Dữ liệu IoT có tính chất High-velocity. Bạn bắt buộc phải có lớp Buffer như Kafka hay Redis Streams để chống nghẽn hệ thống."
        },
        {
            "num": 5,
            "title": "INGESTION TECHNOLOGIES: MQTT, COAP & KAFKA/REDPANDA",
            "bullets": [
                "MQTT (:1883): Giao thức TCP Pub/Sub siêu nhẹ (header 2 bytes), QoS 0/1/2 tin cậy cho mạng chập chờn.",
                "CoAP (:5683 UDP): Giao thức nhị phân RESTful tối ưu cho cảm biến pin yếu (NB-IoT/LPWAN).",
                "Redpanda / Apache Kafka (:9092): Hàng chờ phân tán bất biến chống tràn dữ liệu. Redpanda viết bằng C++, độ trễ thấp hơn 10x và zero JVM overhead."
            ],
            "notes": "MQTT giúp cảm biến gửi tin siêu nhẹ, Mosquitto tiếp nhận, còn Redpanda/Kafka đảm bảo không mất dữ liệu ngay cả khi nghẽn mạng."
        },
        {
            "num": 6,
            "title": "STREAM PROCESSING: WATERMARKING & WINDOWING",
            "bullets": [
                "Event-Time Processing: Luôn xử lý theo Timestamp tạo dữ liệu của cảm biến thay vì giờ của máy chủ.",
                "Bounded-Out-Of-Orderness Watermarking: Watermark(t) = max(Event_Time) - T_delay. Xử lý dữ liệu đến trễ.",
                "Tumbling Window (1m): Cố định không chồng lấn cho thống kê chu kỳ cơ sở.",
                "Sliding Window (5m, trượt 1m): Cửa sổ trượt liên tục tính đạo hàm biến thiên áp suất và tốc độ suy thoái."
            ],
            "notes": "Watermarking là vũ khí bí mật giúp các bạn giải quyết triệt để vấn đề mạng trễ, đảm bảo tính toán cửa sổ chính xác tuyệt đối."
        },
        {
            "num": 7,
            "title": "TIME-SERIES STORAGE: REDIS HOT CACHE VS TIMESCALEDB",
            "bullets": [
                "Redis Hot Cache (< 1ms): Lưu trữ trạng thái tức thời phục vụ Feature Vectors cho AI Model suy luận.",
                "TimescaleDB Hypertables: Biến PostgreSQL thành CSDL chuỗi thời gian phân vùng tự động.",
                "Columnar Compression: Tự động nén dữ liệu cũ giảm 90%+ dung lượng đĩa và hỗ trợ truy vấn SQL chuẩn."
            ],
            "notes": "Mô hình Hot/Cold Storage giúp hệ thống vừa phục vụ AI suy luận tức thì dưới 5ms, vừa lưu trữ dữ liệu lịch sử phục vụ train model."
        },
        {
            "num": 8,
            "title": "THE 5-STEP AI DECISION PIPELINE OVERVIEW",
            "bullets": [
                "1. Feature Extraction: Sliding statistics (Mean, StdDev) & FFT frequency harmonics.",
                "2. Anomaly Detection: Isolation Forest & Deep Autoencoder Reconstruction Error.",
                "3. Root Cause Analysis (RCA): SHAP feature attribution & Causal Knowledge Graphs.",
                "4. AI Agent (LLM + Guardrails): Contextual reasoning with strict safety policy checks.",
                "5. Automated Action Execution: Closed-loop MQTT control dispatches & operator escalation."
            ],
            "notes": "Đây là trái tim của workshop tối nay. 5 bước nối tiếp chuyển hóa hoàn toàn dữ liệu cảm biến thô thành hành động tự động."
        },
        {
            "num": 9,
            "title": "ANOMALY DETECTION: ISOLATION FOREST VS AUTOENCODERS",
            "bullets": [
                "Isolation Forest (Scikit-Learn): Phân lập điểm dị biệt qua cây ngẫu nhiên O(n log n). Cực nhẹ, chạy mượt trên CPU.",
                "Autoencoder Neural Networks: Học biểu diễn trạng thái bình thường. Khi có lỗi mới, Reconstruction Error (MSE) tăng vọt.",
                "ONNX Runtime Acceleration: Tối ưu hóa suy luận mô hình đạt độ trễ < 5ms."
            ],
            "notes": "Isolation Forest nằm ngay trong Scikit-Learn rất nhẹ. Nếu dùng Deep Learning Autoencoder, hãy export ra ONNX Runtime để suy luận nhanh."
        },
        {
            "num": 10,
            "title": "ROOT CAUSE ANALYSIS (RCA) & EXPLAINABLE AI",
            "bullets": [
                "SHAP (SHapley Additive exPlanations): Bóc tách tỷ lệ % đóng góp của từng cảm biến vào điểm bất thường.",
                "Causal Knowledge Graphs: Biểu diễn quan hệ phụ thuộc vật lý (Ví dụ: Bơm hỏng -> Tản nhiệt tăng nhiệt -> Van quá áp).",
                "Lợi ích: Chỉ rõ linh kiện chính bị hỏng thay vì báo lỗi chung chung."
            ],
            "notes": "SHAP values và Knowledge Graphs giúp bạn giải thích cho Giám khảo lý do AI phát hiện đúng linh kiện bị hỏng."
        },
        {
            "num": 11,
            "title": "AI AGENTS, LLMS & DETERMINISTIC SAFETY GUARDRAILS",
            "bullets": [
                "LLM Reasoning (Gemini / OpenAI): Tổng hợp dữ liệu RCA, thông số kỹ thuật và cẩm nang vận hành (SOPs).",
                "Safety Guardrails (Rule Engine & Policies): Kiểm soát an toàn bắt buộc trước khi phát lệnh.",
                "Quy tắc vàng: Tuyệt đối không để LLM tự do gửi lệnh vật lý mà không qua lớp kiểm duyệt an toàn."
            ],
            "notes": "LLM giúp lập luận ngữ cảnh, còn Safety Guardrails bảo đảm hệ thống không bao giờ bị ảo giác gây sự cố vật lý."
        },
        {
            "num": 12,
            "title": "STEP 5: AUTOMATED ACTION EXECUTION & CLOSED-LOOP CONTROL",
            "bullets": [
                "Automated Closed-Loop: Gửi lệnh MQTT/API ngắt thiết bị khẩn cấp, bật quạt phụ hoặc điều chỉnh bơm.",
                "Human-in-the-Loop: Đẩy báo cáo ngôn ngữ tự nhiên về Telegram/Dashboard với nút bấm 1-click 'Approve Action'."
            ],
            "notes": "Vòng lặp hoàn chỉnh! Từ dữ liệu cảm biến ban đầu, hệ thống đã tự động ra lệnh khắc phục sự cố mà không cần con người can thiệp thủ công."
        },
        {
            "num": 13,
            "title": "END-TO-END HACKATHON REFERENCE ARCHITECTURE",
            "bullets": [
                "Data Producer: Python IoT Simulator (paho-mqtt) giả lập đa trạm vật lý.",
                "Broker & Middleware: Mosquitto Broker + Redpanda Event Log + FastAPI.",
                "Stream & AI Engine: Bounded Watermarks + ONNX Models + Fallback Heuristics.",
                "Dashboard: WebSockets + Leaflet Map + Bảng điều hành tự động."
            ],
            "notes": "Các bạn có thể chụp lại Slide này! Đây chính là Blueprint hoàn chỉnh có thể dựng ngay bằng Docker Compose trong 2 giờ."
        },
        {
            "num": 14,
            "title": "RECOMMENDED HACKATHON TECH STACK DEEP-DIVE",
            "bullets": [
                "FastAPI: Web framework phi đồng bộ siêu nhanh cho REST API & WebSockets.",
                "paho-mqtt: Thư viện client gọn nhẹ để tạo trình giả lập IoT trong Python.",
                "TimescaleDB & Redis: Cặp bài trùng lưu trữ Hot/Cold tối ưu.",
                "Leaflet.js & Chart.js: Trực quan hóa bản đồ và dòng dữ liệu thời gian thực."
            ],
            "notes": "Toàn bộ stack được lựa chọn theo tiêu chí: Nhẹ, dễ debug, không tốn RAM và khởi động trong vài giây."
        },
        {
            "num": 15,
            "title": "SECRET WEAPON: DEMO 'LIVE ANOMALY INJECTION'",
            "bullets": [
                "Tạo nút 'Tiêm Sự Cố' (Inject Anomaly) ngay trên giao diện Web.",
                "Kịch bản Pitching 5 phút: 1. Hệ thống bình thường (Xanh) -> 2. Bấm Tiêm Lỗi -> 3. Đồ thị đổi màu, phát hiện sụt áp -> 4. AI chẩn đoán nguyên nhân -> 5. Tự động phát lệnh xử lý thành công."
            ],
            "notes": "Khi chấm thi, Giám khảo chỉ có 5 phút. Hãy cho Giám khảo thấy sự cố xảy ra và hệ thống AI tự động xử lý ngay trước mắt họ!"
        },
        {
            "num": 16,
            "title": "COMMON HACKATHON PITFALLS TO AVOID",
            "bullets": [
                "❌ Pitfall 1: Dành 80% thời gian hàn mạch phần cứng thay vì tập trung vào luồng dữ liệu & AI Engine.",
                "❌ Pitfall 2: Dùng mô hình Deep Learning/LLM quá nặng gây đơ 30 giây khi pitching trực tiếp.",
                "❌ Pitfall 3: Chỉ làm Dashboard tĩnh không có vòng lặp tự động hóa hành động."
            ],
            "notes": "Hãy nhớ: Cuộc thi đánh giá giải pháp AI-Driven Smart Operations, không phải thi hàn mạch phần cứng!"
        },
        {
            "num": 17,
            "title": "LIVE TECHNICAL Q&A & MENTORSHIP",
            "bullets": [
                "Giải đáp trực tiếp mọi thắc mắc về Streaming Pipeline, Watermarking và AI Models.",
                "Tư vấn kiến trúc 1-1 cho ý tưởng cụ thể của từng đội thi.",
                "Hướng dẫn tối ưu hóa kịch bản pitching trước Ban Giám Khảo."
            ],
            "notes": "Bây giờ là thời gian cho các bạn! Hãy đặt bất kỳ câu hỏi nào về khó khăn kỹ thuật mà đội thi của bạn đang gặp phải."
        },
        {
            "num": 18,
            "title": "CLOSING & CONTACT",
            "bullets": [
                "Speaker: Nguyen Duc Tuan (Backend Lead & System Architect)",
                "Event: SEAL Hackathon Summer 2026 • Google Meet",
                "Repository: https://github.com/Pen1112003/AI-Driven-Smart-Operations-Turning-Real-Time-IoT-Data-into-Intelligent-Actions",
                "Thông điệp: Build Smart, Scale Fast, and Drive Intelligent Action!"
            ],
            "notes": "Chúc tất cả các đội thi SEAL Hackathon Summer 2026 xây dựng được những giải pháp Vận hành Thông minh xuất sắc!"
        }
    ]

    for item in SLIDES:
        s_card = doc.add_table(rows=3, cols=1)
        s_card.alignment = WD_TABLE_ALIGNMENT.CENTER
        
        # Header cell
        c_head = s_card.cell(0, 0)
        c_head.width = Inches(6.8)
        set_cell_background(c_head, "15803D")
        set_cell_margins(c_head, 60, 60, 100, 100)
        p_h = c_head.paragraphs[0]
        r_h = p_h.add_run(f"SLIDE {item['num']:02d}: {item['title']}")
        r_h.font.bold = True
        r_h.font.size = Pt(11)
        r_h.font.color.rgb = RGBColor(255, 255, 255)

        # Content cell
        c_body = s_card.cell(1, 0)
        c_body.width = Inches(6.8)
        set_cell_background(c_body, "FFFFFF")
        set_cell_margins(c_body, 80, 80, 120, 120)
        p_b_title = c_body.paragraphs[0]
        p_b_title.add_run("Nội dung hiển thị trên Slide (Slide Content):").font.bold = True
        p_b_title.runs[0].font.size = Pt(9.5)
        p_b_title.runs[0].font.color.rgb = COLOR_NAVY

        for b in item["bullets"]:
            p_bullet = c_body.add_paragraph(style='List Bullet')
            r_b = p_bullet.add_run(b)
            r_b.font.size = Pt(9)
            r_b.font.color.rgb = COLOR_NAVY

        # Notes cell
        c_notes = s_card.cell(2, 0)
        c_notes.width = Inches(6.8)
        set_cell_background(c_notes, "FEF3C7")
        set_cell_margins(c_notes, 60, 60, 120, 120)
        p_n = c_notes.paragraphs[0]
        r_nt = p_n.add_run("🎤 Lời thoại Diễn giả (Speaker Script / Notes): ")
        r_nt.font.bold = True
        r_nt.font.size = Pt(9)
        r_nt.font.color.rgb = COLOR_GOLD

        r_nv = p_n.add_run(f'"{item["notes"]}"')
        r_nv.font.italic = True
        r_nv.font.size = Pt(9)
        r_nv.font.color.rgb = COLOR_NAVY

        doc.add_paragraph() # Spacer

    # 5. SECTION IV: TECH STACK MATRIX
    h4 = doc.add_heading("PHẦN IV: BẢNG MA TRẬN SO SÁNH CÔNG NGHỆ (TECH STACK MATRIX)", level=1)
    h4.runs[0].font.color.rgb = COLOR_PRIMARY

    tech_table = doc.add_table(rows=8, cols=4)
    tech_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_headers = ["Tầng Kiến Trúc", "Công Nghệ", "Ưu Điểm & Vai Trò", "Đánh Giá Cho Hackathon"]
    t_widths = [Inches(1.5), Inches(1.4), Inches(2.6), Inches(1.3)]

    for c_idx, text in enumerate(t_headers):
        cell = tech_table.cell(0, c_idx)
        cell.width = t_widths[c_idx]
        set_cell_background(cell, "0F172A")
        set_cell_margins(cell, 80, 80, 100, 100)
        p = cell.paragraphs[0]
        r = p.add_run(text)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        r.font.size = Pt(9)

    tech_rows = [
        ("Ingestion Protocol", "MQTT (1883)", "Header 2 bytes siêu nhẹ, Pub/Sub linh hoạt, tiết kiệm băng thông.", "⭐ Khuyên dùng số 1"),
        ("Ingestion Protocol", "CoAP (5683 UDP)", "Chạy trên UDP, tối ưu cho cảm biến pin yếu (NB-IoT/LPWAN).", "Tốt cho sensor pin yếu"),
        ("Streaming Buffer", "Redpanda (9092)", "Viết bằng C++, zero JVM, p99 latency cực thấp, tương thích 100% Kafka.", "⭐ Tối ưu cho Docker"),
        ("Streaming Buffer", "Redis Streams", "Chạy trực tiếp trong RAM, sub-millisecond latency, dễ dựng prototype.", "Rất tốt cho demo nhanh"),
        ("Stream Processing", "Async Window Engine", "Tích hợp trực tiếp trong Python, xử lý Watermarking & Windowing linh hoạt.", "⭐ Khuyên dùng cho thi"),
        ("Time-Series DB", "TimescaleDB", "Hypertables phân vùng tự động, nén cột 90%, SQL chuẩn của PostgreSQL.", "⭐ Khuyên dùng số 1"),
        ("AI Anomaly Engine", "Isolation Forest", "Huấn luyện không giám sát, chạy cực nhanh trên CPU, giải thích qua SHAP.", "⭐ Khuyên dùng Baseline")
    ]

    for r_idx, r_data in enumerate(tech_rows, 1):
        bg = "FFFFFF" if r_idx % 2 != 0 else "F8FAFC"
        for c_idx, val in enumerate(r_data):
            cell = tech_table.cell(r_idx, c_idx)
            cell.width = t_widths[c_idx]
            set_cell_background(cell, bg)
            set_cell_margins(cell, 60, 60, 100, 100)
            p = cell.paragraphs[0]
            r = p.add_run(val)
            r.font.size = Pt(8.5)
            r.font.color.rgb = COLOR_NAVY
            if c_idx == 1 or c_idx == 3:
                r.font.bold = True

    doc.add_paragraph()

    # 6. SECTION V: SCORING RUBRIC
    h5 = doc.add_heading("PHẦN V: BẢNG TIÊU CHÍ CHẤM ĐIỂM & CHECKLIST DÀNH CHO THÍ SINH", level=1)
    h5.runs[0].font.color.rgb = COLOR_PRIMARY

    rubric_table = doc.add_table(rows=6, cols=3)
    rubric_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    r_headers = ["Hạng Mục Đánh Giá", "Trọng Số", "Yêu Cầu Kỹ Thuật Đạt Chuẩn"]
    r_widths = [Inches(2.2), Inches(1.0), Inches(3.6)]

    for c_idx, text in enumerate(r_headers):
        cell = rubric_table.cell(0, c_idx)
        cell.width = r_widths[c_idx]
        set_cell_background(cell, "15803D")
        set_cell_margins(cell, 80, 80, 100, 100)
        p = cell.paragraphs[0]
        r = p.add_run(text)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        r.font.size = Pt(9.5)

    rubric_rows = [
        ("1. Kiến trúc phân tầng & Giao thức IoT", "20%", "Hỗ trợ MQTT/CoAP; có Buffer Kafka/Redpanda chống nghẽn; không thất thoát dữ liệu."),
        ("2. Stream Processing & Watermarking", "25%", "Xử lý Event-Time, Watermark trễ mạng; tính toán đúng cửa sổ Tumbling & Sliding."),
        ("3. Mô hình AI & Chẩn đoán RCA", "25%", "Trích xuất đặc trưng đa biến; phát hiện bất thường Isolation Forest/Autoencoder; chỉ ra linh kiện lỗi qua SHAP/Causal Graph."),
        ("4. Tự động hóa điều hành khép kín", "15%", "AI Agent đưa ra phương án khắc phục và phát lệnh điều khiển thiết bị tự động qua MQTT/Webhook."),
        ("5. Giao diện trực quan & Kỹ năng Demo", "15%", "Dashboard trực quan hóa thời gian thực; trình diễn kịch bản Tiêm Lỗi (Live Anomaly Injection) thuyết phục trước Giám khảo.")
    ]

    for r_idx, r_data in enumerate(rubric_rows, 1):
        bg = "FFFFFF" if r_idx % 2 != 0 else "F8FAFC"
        for c_idx, val in enumerate(r_data):
            cell = rubric_table.cell(r_idx, c_idx)
            cell.width = r_widths[c_idx]
            set_cell_background(cell, bg)
            set_cell_margins(cell, 60, 60, 100, 100)
            p = cell.paragraphs[0]
            r = p.add_run(val)
            r.font.size = Pt(9)
            r.font.color.rgb = COLOR_NAVY
            if c_idx == 1:
                r.font.bold = True

    output_path = "/Users/penpen1112003/AI-Driven_Smart_Operations- _From_Real-Time_IoT_Data_to_Intelligent_Decisions/WORKSHOP_AI_DRIVEN_SMART_OPERATIONS_SLIDE_DECK.docx"
    doc.save(output_path)
    print(f"Successfully generated Word document at: {output_path}")

if __name__ == "__main__":
    create_document()
