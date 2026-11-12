# -*- coding: utf-8 -*-
"""Generate static pages. Replace YOUR_PUBLIC_SITE_URL before publishing."""
from html import escape
from pathlib import Path
from urllib.parse import quote

SITE_URL = "https://japan-mounjaro-directory.netlify.app"
SITE_NAME = "마운자로 원정대"
ROOT = Path(__file__).resolve().parent

CITIES = [
    ("chiba", "지바", "Chiba"),
    ("tokyo", "도쿄", "Tokyo"),
    ("osaka", "오사카", "Osaka"),
    ("fukuoka", "후쿠오카", "Fukuoka"),
    ("sapporo", "삿포로", "Sapporo"),
    ("nagoya", "나고야", "Nagoya"),
    ("kyoto", "교토", "Kyoto"),
]

CLINICS = [
    {
        "city": "tokyo",
        "name": "Nihonbashi Clinic",
        "jp": "日本橋クリニック人形町院",
        "area": "주오구",
        "address": "〒103-0013 東京都中央区日本橋人形町2-30-5 エイム人形町2階",
        "summary": "공식 페이지는 마운자로 전화·온라인 상담과 영어·일본어 대응을 안내합니다. 첫 방문 시 신분증과 온라인 문진이 필요할 수 있으며, 처방 여부는 의사가 판단합니다. 영문 안내는 일본 거주자·방문자를 설명하고, 한국 체류 중 상담 가능 여부는 공식 안내에서 확인되지 않았습니다.",
        "phone": "+81-3-6262-5544",
        "tel": "+81362625544",
        "email": "info@nihonbashi.clinic",
        "hours": "일본 시간: 월·화·목·금 12:00–24:00, 토·일 10:00–16:00, 수요일 휴진. 임시 휴진일과 예약 가능 시간은 공식 달력에 표시됩니다.",
        "booking": "공식 안내에는 온라인 예약 절차와 첫 방문 시 필요한 신분증 이미지·문진 정보가 게시되어 있습니다. LINE 메시지는 예약이 아니라고 안내합니다.",
        "mounjaro": "https://www.nihonbashiclinic.jp/en/mounjaro/",
        "access": "https://www.nihonbashiclinic.jp/en/commercial-disclosures/",
        "links": [
            ("https://web.booking.clius.jp/reserve/nihonbashi-clinic-reserve", "공식 안내 페이지"),
            ("https://lin.ee/8EUX0F0", "공식 LINE"),
        ],
    },
    {
        "city": "tokyo",
        "name": "Shinbashi Ginza Swift Clinic",
        "jp": "新橋銀座スウィフトクリニック",
        "area": "미나토구",
        "address": "〒105-0004 東京都港区新橋1-8-4 丸忠ビル7F-B",
        "summary": "공식 영문 페이지에서 온라인 마운자로 상담과 영문 예약 양식을 안내합니다. 예약 뒤 사전 문진을 작성하며, 병원 안내상 예약 시스템·문진은 일본어일 수 있어 LINE으로 도움을 문의할 수 있습니다.",
        "phone": "+81-3-5962-8738",
        "tel": "+81359628738",
        "email": "공식 페이지에서 이메일 문의처를 확인하지 못했습니다.",
        "hours": "일본 시간: 평일 14:00–21:00, 주말·공휴일 10:00–18:00. 운영시간은 변경될 수 있습니다.",
        "booking": "공식 영문 안내에는 온라인 예약 양식이 있으며, 사전 문진은 일본어일 수 있습니다.",
        "mounjaro": "https://www.swift-clinic.com/en/online/mounjaro",
        "access": "https://www.swift-clinic.com/en/access",
        "links": [
            ("https://booking.swift-clinic.com/en/booking?openexternalbrowser=1&openExternalBrowser=1&from=swift", "공식 안내 페이지"),
            ("https://liff.line.me/1656697392-Rr3pNqYq/landing?follow=%40209qcaxd&lp=AD0ZCj&liff_id=1656697392-Rr3pNqYq", "공식 LINE"),
            ("https://www.iryou.teikyouseido.mhlw.go.jp/znk-web/juminkanja/S2430/initialize?kikanCd=2136000522&kikanKbn=2&prefCd=13", "일본 의료정보망"),
        ],
    },
    {
        "city": "tokyo",
        "name": "Drip Medical",
        "jp": "Drip Medical Beauty",
        "area": "미나토구",
        "address": "〒105-0013 東京都港区浜松町1-27-14 サン・キツカワビル3F",
        "summary": "공식 마운자로 페이지는 의사의 적합성 평가를 거치는 온라인 상담을 안내하며, 예약 화면은 일본어로 열린다고 명시합니다. 예약 뒤 처방 가능 여부는 의료진이 판단합니다.",
        "phone": "+81-3-6452-9113",
        "tel": "+81364529113",
        "email": "공식 안내에서 이메일 문의처를 확인하지 못했습니다.",
        "hours": "일본 시간 10:30–19:30, 월·수 휴무. 확인한 공식 안내에는 전화 응대 가능 시간이 별도로 표시되어 있지 않습니다.",
        "booking": "온라인 예약 페이지는 일본어로 제공됩니다.",
        "mounjaro": "https://dripmed.jp/en/treatments/mounjaro",
        "access": "https://dripmed.jp/en/access",
        "links": [
            ("https://reservation.medical-force.com/c/b465b3ed69a5454da5c64e8213450625", "공식 안내 페이지"),
            ("https://lin.ee/FUKKV0v", "공식 LINE"),
        ],
    },
    {
        "city": "tokyo",
        "name": "Tokyo Online Clinic",
        "jp": "東京オンラインクリニック（池袋サンシャイン通り皮膚科）",
        "area": "도시마구",
        "address": "〒170-0013 東京都豊島区東池袋1丁目12-11 Ogsビル11階",
        "summary": "공식 마운자로 페이지는 온라인 진료 정보를 게시하며, 처방은 의료진 판단에 따라 달라질 수 있다고 설명합니다.",
        "phone": "+81-3-6771-7809",
        "tel": "+81367717809",
        "email": "info@tokyo-online-clinic.com",
        "hours": "공식 페이지별 운영시간이 다릅니다(10:30–19:30, 11:00–20:00 등). 공식 페이지별 운영시간 표기가 다릅니다.",
        "booking": "공식 페이지와 예약 시스템은 일본어 중심이며, 한국 거주자 상담 가능 여부는 공식 안내에서 확인되지 않았습니다.",
        "mounjaro": "https://tokyo-online-clinic.com/medicine/mounjaro/",
        "access": "https://tokyo-online-clinic.com/contact/",
        "links": [
            ("https://reserve.marchss.com/#/reservation/71755267-9332-4999-93be-1d29506d0688/?clinicId=a93a338efd064e079d210b6b7c197a2e&utm_source=official&utm_medium=organic", "공식 안내 페이지"),
            ("https://lin.ee/zWCaCV7", "공식 LINE"),
        ],
    },
    {
        "city": "tokyo",
        "name": "Mirai Medical Clinic Setagaya",
        "jp": "ミライメディカルクリニック（世田谷・一般社団法人新玄会）",
        "area": "세타가야구",
        "address": "〒154-0004 東京都世田谷区太子堂2丁目12-2 T-one世田谷ビル",
        "summary": "공식 한국어 페이지는 예약·진료·사후 상담을 한국어로 진행하고, 일본 여행 일정이 정해지면 한국에 있을 때 미리 진료할 수 있다고 적습니다. 처방약 수령 장소는 일본 내 호텔·체류지라고 안내합니다. 후쿠오카의 Mirai Medical Clinic과는 다른 기관입니다. 처방 여부는 의사가 판단합니다.",
        "phone": "공식 페이지에서 전화번호를 확인하지 못했습니다.",
        "email": "공식 페이지에서 이메일 주소를 확인하지 못했습니다.",
        "hours": "온라인 진료는 24시간 365일이라고 적혀 있습니다.",
        "booking": "예약 화면에서 일본 체류지 주소를 넣는 절차가 안내되어 있습니다. 직원 국적은 확인되지 않았습니다.",
        "korea_consult": "공식 질문 답변은 한국에 있을 때 출발 전 진료가 가능하다고 적습니다. 약은 일본 내 호텔·체류지에서 받는다고 안내하며, 한국으로 보낸다는 안내는 없습니다. 처방 여부는 의사가 판단합니다.",
        "mounjaro": "https://mirai-medical.clinic/ko/mounjaro/",
        "access": "https://mirai-medical.clinic/ko/mounjaro/",
        "links": [
            ("https://mirai-medical.clinic/ko/mounjaro/", "공식 안내 페이지"),
        ],
    },
    {
        "city": "tokyo",
        "name": "Japan Net Clinic",
        "jp": "ビューティーオンクリニック銀座",
        "area": "주오구",
        "address": "〒104-0061 東京都中央区銀座8-9-7 HULIC & New GINZA 8 11F",
        "summary": "공식 페이지는 한국어·영어·일본어로 진료하는 한국인 의사가 직접 진료한다고 적습니다. 초진과 재진 모두 온라인 진료를 신청할 수 있고, 의사가 대면 진료가 필요하다고 판단할 수 있다고 안내합니다. 기본 대상은 일본 내 주소가 있는 사람이며, 한국 거주 여행객 문의에는 일본 체류 중 진료라고 답합니다. 해외 배송은 제공하지 않는다고 적혀 있습니다.",
        "phone": "+81-3-6281-4250",
        "tel": "+81362814250",
        "email": "ginzayoyakukanri@gmail.com",
        "hours": "진료·수령 시간 10:00–20:40. 2026년 12월 2일까지 수요일 휴진, 12월 9일부터 수요일도 진료한다고 적혀 있습니다.",
        "booking": "카카오톡 ID japanclinic. LINE ID는 @800qlpmi로 적혀 있으나 공개된 LINE 주소는 확인하지 못했습니다. 원장 외 직원의 국적과 상주 여부는 확인되지 않았습니다.",
        "korea_consult": "한국에 있는 상태에서 원격 진료가 가능하다고 확인된 문장은 없습니다. 한국 거주 여행객에 대한 답변은 일본 체류 중 진료를 상담할 수 있다는 내용입니다. 처방 여부는 의사가 판단합니다.",
        "mounjaro": "https://japannetclinic.com/ko/online/",
        "access": "https://japannetclinic.com/",
        "links": [
            ("https://japannetclinic.com/ko/online/", "공식 온라인 안내"),
            ("https://japannetclinic.com/", "공식 안내 페이지"),
        ],
    },
    {
        "city": "osaka",
        "name": "Daibikai Clinic Shinsaibashi",
        "jp": "大美会クリニック 心斎橋本院",
        "area": "주오구",
        "address": "〒542-0083 大阪府大阪市中央区東心斎橋2-8-28 周防町GEOビル3F",
        "summary": "공식 마운자로 안내와 일본어 예약 화면에 온라인 진료 및 마운자로 상담 항목이 표시됩니다. 처방은 의사의 판단에 따릅니다.",
        "phone": "0120-373-889",
        "tel": "0120373889",
        "email": "info_shinsaibashi@daibikai.com",
        "hours": "공식 페이지와 예약 시스템의 운영시간 표기가 다릅니다. 병원 페이지: 월–토 11:00–21:00, 일·공휴일 11:00–20:00. 예약 시스템은 각각 11:00–20:00, 11:00–19:00로 표기합니다. 예약 시스템에는 다른 운영시간이 표시되어 있습니다.",
        "booking": "일본어 예약 시스템에 온라인 마운자로 상담 항목이 있습니다.",
        "mounjaro": "https://osaka-bc.com/menu/mounjaro/",
        "access": "https://osaka-bc.com/clinic/shinsaibashi/",
        "links": [
            ("https://clinics-app.com/clinic/5d68db1677f75e2beac6a76f/reservation?method=online", "공식 안내 페이지"),
            ("https://osaka-bc.com/contact/", "공식 문의"),
        ],
    },
    {
        "city": "osaka",
        "name": "Ai Clinic Shinsaibashi",
        "jp": "Aiクリニック心斎橋",
        "area": "주오구",
        "address": "〒542-0081 大阪府大阪市中央区南船場3丁目11-18 Osaka Metro 心斎橋ビル7F",
        "summary": "공식 마운자로 안내는 온라인·내원 진료를 모두 안내하고 LINE으로 희망 내용을 문의하는 절차를 설명합니다. 처방 여부는 상담 결과에 따라 달라질 수 있습니다.",
        "phone": "+81-6-6121-7600",
        "tel": "+81661217600",
        "email": "공식 페이지에서 이메일 문의처를 확인하지 못했습니다.",
        "hours": "일본 시간 10:00–19:00, 일·공휴일은 18:30까지. 수요일 휴진(공휴일이면 진료 안내가 있을 수 있음).",
        "booking": "공식 LINE 및 일본어 웹 페이지에 상담 관련 정보가 게시되어 있습니다.",
        "mounjaro": "https://saclinic.net/glp-1/",
        "access": "https://saclinic.net/contact/",
        "links": [
            ("https://shinsaibashi-ai.b4a.clinic/", "공식 안내 페이지"),
            ("https://page.line.me/bvq0559a?openQrModal=true", "공식 LINE"),
        ],
    },
    {
        "city": "osaka",
        "name": "ONE CLINIC Umeda",
        "jp": "ONE CLINIC 梅田",
        "area": "기타구",
        "address": "〒530-0027 大阪府大阪市北区堂山町18-2 若杉東梅田ビル3階・5階（美容受付は3階）",
        "summary": "공식 메디컬 다이어트 페이지에 마운자로와 온라인 진료 안내가 있습니다. 예약 시스템에는 온라인 다이어트 외래 항목이 표시되며, 처방은 진료 후 판단됩니다.",
        "phone": "+81-6-6311-5770",
        "tel": "+81663115770",
        "email": "공식 페이지에서 이메일 문의처를 확인하지 못했습니다.",
        "hours": "공식 병원 안내: 월·수–일 10:00–13:00, 14:00–19:30. 화요일·일부 주말 휴진 표기가 있어 예약 화면에는 다른 운영시간이 표시되어 있습니다.",
        "booking": "일본어 예약 시스템에 온라인 다이어트 외래가 있으며 공식 LINE 경로가 게시되어 있습니다.",
        "mounjaro": "https://one-clinic-umeda.com/medical-diet/",
        "access": "https://one-clinic-umeda.com/doctor-and-clinic/",
        "links": [
            ("https://clinics-app.com/clinic/5e3137bd110b8444bb5bc454/reservation?method=online", "공식 안내 페이지"),
            ("https://line.me/R/ti/p/@389toqux?ts=04191222&oat_content=url", "공식 LINE"),
        ],
    },
    {
        "city": "fukuoka",
        "name": "M Medical Clinic Fukuoka",
        "jp": "Mメディカルクリニック福岡",
        "area": "하카타구",
        "address": "〒812-0013 福岡県福岡市博多区博多駅東2丁目5-33 ゲートスクエア博多駅前2階",
        "summary": "공식 마운자로 안내는 온라인 진료 후 의사가 처방 여부를 판단한다고 설명합니다. 예약·상담 관련 공식 페이지는 일본어로 제공됩니다.",
        "phone": "+81-92-441-5003",
        "tel": "+81924415003",
        "email": "공식 페이지에서 이메일 문의처를 확인하지 못했습니다.",
        "hours": "일본 시간: 평일 10:00–18:00, 토·일 09:00–17:00, 공휴일은 비정기 휴진.",
        "booking": "공식 WEB 페이지에는 온라인 상담과 예약 관련 정보가 있고, 공식 LINE 채널도 게시되어 있습니다.",
        "mounjaro": "https://m-fukuoka.com/treatment/detail/20241213114429/",
        "access": "https://m-fukuoka.com/access/",
        "links": [
            ("https://reservation.medical-force.com/c/bb5608f2e21b44c693481da92cd75dee?landing_event_id=35d4b66a-4feb-4632-998e-4d1142f8370d", "공식 안내 페이지"),
            ("https://page.line.me/836jcgir?oat__id=5088960&openQrModal=true", "공식 LINE"),
        ],
    },
    {
        "city": "fukuoka",
        "name": "Mirai Medical Clinic",
        "jp": "ミライメディカルクリニック",
        "area": "하카타구",
        "address": "〒812-0027 福岡県福岡市博多区下川端町3-1 博多リバレイン1F",
        "summary": "공식 온라인 다이어트 안내에 마운자로 진료와 온라인 예약 경로가 있습니다. 의사 진료를 거치며 상담 결과에 따라 처방되지 않을 수 있습니다. 한국 거주자의 원격상담 가능 여부는 이 기관의 공식 안내에서 확인되지 않았습니다. 도쿄 세타가야의 Mirai Medical Clinic Setagaya와는 다른 기관입니다.",
        "phone": "+81-92-707-1111",
        "tel": "+81927071111",
        "email": "공식 페이지에서 이메일 주소를 확인하지 못했습니다.",
        "hours": "일본 시간 10:00–14:00(접수 13:30까지), 15:30–19:00(접수 18:30까지). 요일별 진료일은 공식 안내에 따라 달라질 수 있습니다.",
        "booking": "일본어 페이지·예약 시스템과 LINE·문의 양식이 게시되어 있습니다.",
        "mounjaro": "https://miraimedical.com/treatment/online/diet/",
        "access": "https://miraimedical.com/access/",
        "links": [
            ("https://clinics-app.com/clinic/622ee5023d54a12871768d66", "공식 안내 페이지"),
            ("https://page.line.me/613czwhp?openQrModal=true", "공식 LINE"),
            ("https://miraimedical.com/contact", "문의 양식"),
        ],
    },
    {
        "city": "fukuoka",
        "name": "Clara Beauty Clinic Fukuoka Tenjin",
        "jp": "クララ美容皮膚科 福岡天神院",
        "area": "주오구",
        "address": "〒810-0001 福岡県福岡市中央区天神3丁目4-10 天神西茂ビル3階",
        "summary": "공식 페이지는 마운자로 온라인 진료 후 처방을 안내합니다. 전화번호는 확인한 공식 페이지에 게시되지 않아 공식 LINE 경로를 함께 표시했습니다.",
        "phone": "공식 페이지에서 전화번호를 확인하지 못했습니다.",
        "email": "공식 페이지에서 이메일 문의처를 확인하지 못했습니다.",
        "hours": "공식 페이지에 운영시간이 명확히 표시되어 있지 않으며 LINE 경로가 게시되어 있습니다.",
        "booking": "공식 마운자로 페이지와 LINE에 온라인 상담 관련 정보가 게시되어 있습니다.",
        "mounjaro": "https://clarabeautyclinic.jp/fukuoka/treatment_example/treatment_example-1424/",
        "access": "https://clarabeautyclinic.jp/fukuoka/",
        "links": [
            ("https://line.me/R/ti/p/@809gyobs", "공식 LINE"),
        ],
    },
    {
        "city": "sapporo",
        "name": "Clara Beauty Clinic Sapporo",
        "jp": "クララビューティクリニック札幌院",
        "area": "기타구",
        "address": "〒060-0806 北海道札幌市北区北6条西4丁目2-7 J1札幌北口ビル2階",
        "summary": "공식 마운자로 안내는 온라인 영상 상담 절차를 소개합니다. 처방은 의사 판단에 달려 있으며 보장되지 않습니다.",
        "phone": "+81-11-211-1244",
        "tel": "+81112111244",
        "email": "info@clarabeautyclinic.jp",
        "hours": "일본 시간 11:00–20:00. 연말연시 외 운영 안내가 있으나 온라인 상담 가능 시간은 공식 안내에 별도로 표시되어 있지 않습니다.",
        "booking": "공식 안내에는 온라인 상담 경로와 일본어 예약 정보가 게시되어 있습니다.",
        "mounjaro": "https://clarabeautyclinic.jp/sapporo/menu/medicine/manjaro/",
        "access": "https://clarabeautyclinic.jp/sapporo/contact/",
        "links": [
            ("https://line.me/R/ti/p/%40yoy5225w", "공식 LINE"),
            ("https://clarabeautyclinic.jp/sapporo/manjaro-lp/", "공식 안내"),
        ],
    },
    {
        "city": "sapporo",
        "name": "Asteria Clinic",
        "jp": "アステリアクリニック",
        "area": "주오구",
        "address": "〒060-0061 北海道札幌市中央区南1条西4丁目20-1 ビッグタワー大通公園2F",
        "summary": "공식 마운자로 안내는 온라인 상담·처방 절차를 게시합니다. 별도의 온라인 진료 안내는 예약 후 LINE 등록과 화상 상담을 설명합니다. 처방 여부는 의사 판단에 따릅니다.",
        "phone": "0120-706-860 (일본 국내 무료전화)",
        "tel": "0120706860",
        "email": "info@asteria-clinic.jp",
        "hours": "일본 시간 온라인 진료 안내: 11:00–15:00, 16:00–19:00 등. 문의·고지 페이지에는 11:00–20:00 표기도 있어 예약 화면에는 다른 운영시간이 표시되어 있습니다.",
        "booking": "일본어 온라인 예약 페이지와 공식 LINE 등록 안내가 게시되어 있으며, 확인한 페이지에는 LINE 직접 주소가 표시되지 않았습니다.",
        "mounjaro": "https://asteria-clinic.jp/article/cat-diet/online-mounjaro-rybelsus-glp1/",
        "access": "https://online.asteria-clinic.jp/",
        "links": [
            ("https://asteria-clinic.reserve.ne.jp/sp/", "공식 안내 페이지"),
            ("https://asteria-clinic.jp/specified/", "공식 운영자 정보"),
        ],
    },
    {
        "city": "nagoya",
        "name": "Velvaere Honjin Clinic",
        "jp": "ヴェルヴァーレ本陣クリニック",
        "area": "나카무라구",
        "address": "〒453-0041 愛知県名古屋市中村区本陣通2-19",
        "summary": "공식 페이지는 마운자로 온라인 진료를 명시하고, 온라인 진료 뒤 의사가 처방 가능 여부를 판단한다고 안내합니다.",
        "phone": "+81-52-414-5151",
        "tel": "+81524145151",
        "email": "공식 페이지에서 이메일 문의처를 확인하지 못했습니다.",
        "hours": "일본 시간: 월–금 09:30–12:30, 14:00–18:30; 토 09:00–13:00, 14:00–17:00; 일 09:30–12:30. 일요일 오후·공휴일 휴진.",
        "booking": "전용 온라인 예약 화면과 일본어 안내, 공식 LINE 문의 경로가 게시되어 있습니다.",
        "mounjaro": "https://velvaere-clinic.com/menu/%E3%83%9E%E3%83%B3%E3%82%B8%E3%83%A3%E3%83%AD%EF%BC%88%E3%82%AA%E3%83%B3%E3%83%A9%E3%82%A4%E3%83%B3%E8%A8%BA%E7%99%82%E5%AF%BE%E5%BF%9C%EF%BC%89/",
        "access": "https://velvaere-clinic.com/clinic.html",
        "links": [
            ("https://patient.digikar-smart.jp/institutions/3b36c9ca-b3a5-4f68-8c33-6457b90f82a0/reserve?treatmentMenuId=5898de53-5c09-4637-8527-252c2f7fa3ed", "공식 안내 페이지"),
            ("https://line.me/R/ti/p/%40717iupro", "공식 LINE"),
        ],
    },
    {
        "city": "nagoya",
        "name": "MARU Clinic",
        "jp": "MARUクリニック 内科・糖尿病内科",
        "area": "나카구",
        "address": "〒460-0002 愛知県名古屋市中区丸の内2丁目16-8 フレア丸の内4階",
        "summary": "공식 진료 안내에 온라인 마운자로 처방을 게시합니다. 진찰 뒤 의사가 처방 여부를 결정합니다.",
        "phone": "+81-52-253-7715",
        "tel": "+81522537715",
        "email": "공식 페이지에서 이메일 문의처를 확인하지 못했습니다.",
        "hours": "일본 시간: 월·화·목·금 09:00–12:30, 16:00–19:30; 토·일 09:00–13:00; 수·공휴일 및 주말 오후 휴진.",
        "booking": "일본어 WEB 예약 시스템과 공식 LINE 경로가 게시되어 있습니다.",
        "mounjaro": "https://nagoya-maruclinic.com/ownexpense/",
        "access": "https://nagoya-maruclinic.com/about/",
        "links": [
            ("https://ssc.doctorqube.com/nagoya-maruclinic/select.html", "공식 안내 페이지"),
            ("https://line.me/R/ti/p/@870zrcjk", "공식 LINE"),
        ],
    },
    {
        "city": "nagoya",
        "name": "Hosokawa Surgery Clinic",
        "jp": "医療法人細川外科クリニック",
        "area": "나카무라구",
        "address": "〒453-0812 愛知県名古屋市中村区西米野町1丁目75-2",
        "summary": "공식 온라인 진료 페이지와 병원 안내에서 마운자로 온라인 진료를 확인했습니다. 온라인 상담에서 의사가 적합성을 판단하며 처방이 보장되는 것은 아닙니다.",
        "phone": "+81-52-481-9921",
        "tel": "+81524819921",
        "email": "공식 페이지에서 이메일 문의처를 확인하지 못했습니다.",
        "hours": "온라인 진료와 내원 진료 시간이 다를 수 있습니다. 온라인 진료와 내원 진료의 시간이 다를 수 있으며, 공식 문의 양식이 공개되어 있습니다.",
        "booking": "온라인 메디컬 다이어트 안내와 공식 문의 양식이 게시되어 있습니다.",
        "mounjaro": "https://www.hosoge-online.com/medical_diet",
        "access": "https://www.hosoge.com/contact",
        "links": [
            ("https://www.hosoge-online.com/contact", "온라인 진료 문의"),
            ("https://www.hosoge.com/news_detail?actual_object_id=347", "공식 공지"),
        ],
    },
    {
        "city": "kyoto",
        "name": "Kajiyama Internal Medicine Clinic",
        "jp": "梶山内科クリニック",
        "area": "시모교구",
        "address": "〒600-8898 京都市下京区西七条東御前田町20番地1 京都五条クリニックビル2階",
        "summary": "공식 비만 진료 페이지에서 마운자로 대면·온라인 상담을 안내합니다. 온라인 상담 예약은 LINE을 통해야 한다고 설명하며, 진료 뒤 처방 여부는 의사 판단에 달려 있습니다.",
        "phone": "+81-75-326-8739",
        "tel": "+81753268739",
        "email": "공식 페이지에서 이메일 문의처를 확인하지 못했습니다.",
        "hours": "일본 시간: 월–수·금 09:00–13:00, 16:00–19:00; 토 09:00–13:00. 목·토 오후·일·공휴일 휴진. 온라인 상담 시간은 공식 안내에 별도로 표시되어 있지 않습니다.",
        "booking": "공식 안내에는 LINE을 통한 온라인 상담 절차가 설명되어 있습니다.",
        "mounjaro": "https://www.kajiyama-clinic.com/obesity",
        "access": "https://www.kajiyama-clinic.com/clinic",
        "links": [
            ("https://line.me/R/ti/p/%40162edzgv", "공식 LINE"),
        ],
    },
    {
        "city": "kyoto",
        "name": "Kyoto Karasuma Buffalo ED Clinic",
        "jp": "京都烏丸バッファローEDクリニック",
        "area": "시모교구",
        "address": "〒600-8421 京都市下京区童侍者町161 綾小路スクエア702号室",
        "summary": "공식 마운자로 안내에는 온라인 상담 절차와 LINE 경로가 게시되어 있습니다. 처방은 의사 평가에 따라 달라질 수 있습니다.",
        "phone": "+81-75-585-5973",
        "tel": "+81755855973",
        "email": "공식 페이지에서 이메일 문의처를 확인하지 못했습니다.",
        "hours": "일본 시간: 월–토 15:00–20:00, 일·공휴일 휴진. 온라인 상담 시간은 공식 안내에 별도로 표시되어 있지 않습니다.",
        "booking": "마운자로 전용 LINE에는 온라인 상담 양식이 있으며, 일반 문의용 LINE과 별도로 안내되어 있습니다.",
        "mounjaro": "https://buffalo-kyoto.jp/garlic-injection",
        "access": "https://buffalo-kyoto.jp/access",
        "links": [
            ("https://lin.ee/7CZAjJR", "공식 안내 페이지"),
            ("https://line.me/R/ti/p/%40964ujuxs", "공식 LINE 문의"),
        ],
    },
    {
        "city": "kyoto",
        "name": "Daibikai Clinic Kyoto Karasuma",
        "jp": "大美会クリニック 京都烏丸院",
        "area": "시모교구",
        "address": "〒600-8006 京都市下京区四条通柳馬場西入 立売中之町92 AOKIビル6F",
        "summary": "공식 마운자로 페이지는 온라인 상담 흐름을 안내하고, 예약 시스템에는 마운자로 상담용 온라인 다이어트 외래가 있습니다. 처방은 상담 후 의료진이 판단합니다.",
        "phone": "0120-373-889 (일본 국내 무료전화)",
        "tel": "0120373889",
        "email": "info_kyotokarasuma@daibikai.com",
        "hours": "공식 병원 안내: 월–토 11:00–21:00, 일·공휴일 11:00–20:00. 연결된 예약 페이지는 더 짧은 시간을 표기하므로 예약 화면에는 다른 운영시간이 표시되어 있습니다.",
        "booking": "일본어 온라인 다이어트 외래 정보가 게시되어 있습니다.",
        "mounjaro": "https://osaka-bc.com/menu/mounjaro/",
        "access": "https://osaka-bc.com/clinic/kyoto-karasuma/",
        "links": [
            ("https://clinics-app.com/clinic/5f110ce394552f462b4733b7/reservation?method=online", "공식 안내 페이지"),
        ],
    },
    {
        "city": "chiba",
        "name": "HANI CLINIC",
        "jp": "HANI CLINIC（運営: 株式会社メドマルジェ）",
        "area": "이치카와시",
        "address": "〒272-0826 千葉県市川市真間3-5-19（소개 페이지에 적힌 운영 법인 소재지）",
        "summary": "공식 한국어 소개는 한국에 있을 때와 일본에 체류할 때 모두 일본 현지 의사의 온라인 진료를 받을 수 있다고 적습니다. 처방 여부는 의사가 판단합니다.",
        "phone": "공식 페이지에서 전화번호를 확인하지 못했습니다. 특정상거래법 표기는 요청 시 공개한다고 적습니다.",
        "email": "info@hani-clinic.com",
        "hours": "공식 페이지에서 진료 시간을 확인하지 못했습니다.",
        "booking": "공식 질문 답변은 일본으로 출발하기 전 한국에서 온라인 진료가 가능하다고 적습니다. 이용약관은 이용자를 일본 국내에서 서비스를 이용하는 사람으로 정의하므로, 적용 범위는 공식 페이지에서 다시 확인해야 합니다.",
        "korea_consult": "공식 소개는 한국에 있을 때도 온라인 진료가 가능하다고 적습니다. 처방 여부는 의사가 판단합니다.",
        "mounjaro": "https://hani-clinic.com/",
        "access": "https://hani-clinic.com/about",
        "links": [
            ("https://hani-clinic.com/", "공식 안내 페이지"),
            ("https://hani-clinic.com/about", "클리닉 소개"),
        ],
    },
    {
        "city": "fukuoka",
        "name": "FONTANA CLINIC Tenjin",
        "jp": "폰타나클리닉 텐진",
        "area": "주오구",
        "address": "〒810-0021 福岡県福岡市中央区今泉1-18-23 CASA FONTANA 2F",
        "summary": "공식 한국어 페이지는 한국어 대응 스태프가 매일 있고, 한국에 있는 동안 온라인 진료를 예약할 수 있다고 적습니다. 직원의 국적은 확인되지 않았습니다. 처방 여부는 의사가 판단합니다.",
        "phone": "공식 한국어 페이지에서 전화번호를 확인하지 못했습니다.",
        "email": "공식 한국어 페이지에서 이메일 주소를 확인하지 못했습니다.",
        "hours": "공식 한국어 페이지에 운영시간이 따로 적혀 있지 않습니다.",
        "booking": "한국어 상담 경로로 카카오톡 ID fontanaclinic이 안내되어 있습니다.",
        "korea_consult": "공식 질문 답변은 한국에 체류하는 동안 예약과 온라인 진료가 가능하다고 적습니다. 처방 여부는 의사가 판단합니다.",
        "mounjaro": "https://fontana-clinic.jp/kr/",
        "access": "https://fontana-clinic.jp/kr/",
        "links": [
            ("https://fontana-clinic.jp/kr/", "공식 안내 페이지"),
        ],
    },
    {
        "city": "osaka",
        "name": "MIL CLINIC OSAKA",
        "jp": "MIL CLINIC OSAKA（医療法人継桜会）",
        "area": "주오구",
        "address": "〒542-0086 大阪府大阪市中央区西心斎橋1-5-27 7F",
        "summary": "공식 한국어 페이지는 일본에 거주하지 않는 외국인도 출발 전 온라인 상담이 가능하다고 적습니다. 온라인 진료 언어는 일본어·영어로 안내되어 있습니다. 처방 여부는 의사가 판단합니다.",
        "phone": "+81-6-6786-8880",
        "tel": "+81667868880",
        "email": "공식 페이지에서 이메일 주소를 확인하지 못했습니다.",
        "hours": "일본 시간 10:00–19:00. 비정기 휴무가 있다고 적혀 있습니다.",
        "booking": "공식 페이지는 출발 전 온라인 상담과 여권 확인을 안내합니다.",
        "korea_consult": "공식 한국어 페이지는 일본 비거주 외국인의 출발 전 온라인 상담이 가능하다고 적습니다. 한국 거주만 따로 한정한 문장은 없습니다. 처방 여부는 의사가 판단합니다.",
        "mounjaro": "https://mil-clinic.com/lp/mounjaro-kr/",
        "access": "https://mil-clinic.com/lp/mounjaro-kr/",
        "links": [
            ("https://mil-clinic.com/lp/mounjaro-kr/", "공식 안내 페이지"),
        ],
    },
]


def e(value):
    return escape(str(value), quote=True)


def ext(url, label, cls):
    return (
        f'<a class="{cls}" href="{e(url)}" target="_blank" rel="noopener noreferrer">{e(label)}</a>'
    )


def map_url(address):
    return "https://www.google.com/maps/search/?api=1&query=" + quote(address)


def phone_html(clinic):
    phone = clinic["phone"]
    tel = clinic.get("tel")
    if tel and not phone.startswith("공식 페이지"):
        html = f'<a href="tel:{e(tel)}">{e(phone)}</a>'
        if phone.startswith("0120"):
            html += '<span class="mini-note">일본 국내 무료전화 번호로, 해외에서는 연결되지 않을 수 있습니다.</span>'
        return html
    return e(phone)


def row(label, value_html):
    return f'<div class="detail"><dt>{e(label)}</dt><dd>{value_html}</dd></div>'


PHRASES = [
    ("한국 거주자도 상담할 수 있나요?", "韓国在住ですが、オンライン診療を受けることは可能でしょうか？", "한국에 거주하고 있는데 온라인 진료를 받을 수 있을까요?"),
    ("한국에 체류 중에도 진료가 가능한가요?", "現在、韓国に滞在していますが、韓国からオンライン診療を受けることは可能でしょうか？", "현재 한국에 체류 중인데, 한국에서 온라인 진료를 받을 수 있을까요?"),
    ("한국어 또는 영어 상담이 가능한가요?", "韓国語または英語での対応は可能でしょうか？", "한국어 또는 영어로 상담할 수 있을까요?"),
    ("일본 내 주소가 반드시 필요한가요?", "オンライン診療を受けるために、日本国内の住所は必要でしょうか？", "온라인 진료를 받으려면 일본 국내 주소가 필요한가요?"),
    ("본인 확인에 필요한 서류는 무엇인가요?", "本人確認に必要な書類を教えてください。", "본인 확인에 필요한 서류를 알려 주세요."),
    ("해외 신용카드 결제가 가능한가요?", "海外発行のクレジットカードで支払うことは可能でしょうか？", "해외에서 발급한 신용카드로 결제할 수 있을까요?"),
    ("온라인 진료는 영상통화인가요?", "オンライン診療はビデオ通話で行われますか？", "온라인 진료는 영상 통화로 진행되나요?"),
    ("일본어 외 다른 언어 지원이 가능한가요?", "日本語以外の言語での対応は可能でしょうか？", "일본어 이외의 언어로 상담할 수 있을까요?"),
]


def has_line(clinic):
    for url, label in clinic["links"]:
        low_url = url.lower()
        if "line" in label.lower() or "lin.ee" in low_url or "line.me" in low_url:
            return True
    return False


def phrase_items():
    items = []
    for index, (title, jp, ko) in enumerate(PHRASES, start=1):
        items.append(
            f"""<article class="phrase">
              <p class="phrase-kicker">{index:02d}. {e(title)}</p>
              <p class="phrase-jp" lang="ja">{e(jp)}</p>
              <p class="phrase-ko">{e(ko)}</p>
              <div class="phrase-actions">
                <button class="copy-button phrase-copy" type="button" data-copy="{e(jp)}" data-copied="일본어 문장을 복사했습니다.">일본어 복사</button>
                <p class="copy-status" data-copy-status role="status"></p>
              </div>
            </article>"""
        )
    return "\n".join(items)


def line_details():
    return f"""<details class="line-guide">
            <summary>LINE 문의 시 참고할 질문</summary>
            <p class="line-guide-note">공식 LINE에 물어볼 때 쓰는 문장 예시입니다. 이 기관의 답변이나 상담 가능 여부가 아닙니다.</p>
            {phrase_items()}
          </details>"""


CHECKED = {
    "HANI CLINIC": "2026-11-12",
    "FONTANA CLINIC Tenjin": "2026-11-12",
    "MIL CLINIC OSAKA": "2026-11-12",
    "Mirai Medical Clinic Setagaya": "2026-11-12",
    "Japan Net Clinic": "2026-11-12",
}
CITY_NAME = {city_id: name for city_id, name, _en in CITIES}


def status_item(label, value, kind):
    return f'<li><span>{e(label)}</span><strong class="badge {kind}">{e(value)}</strong></li>'


def korea_status(clinic):
    if clinic["name"] in ("HANI CLINIC", "FONTANA CLINIC Tenjin", "Mirai Medical Clinic Setagaya"):
        return "안내 있음", "is-yes"
    if clinic["name"] == "MIL CLINIC OSAKA":
        return "출발 전 안내", "is-mid"
    return "미확인", "is-unknown"


def korean_status(clinic):
    if clinic["name"] == "Japan Net Clinic":
        return "한국인 의사", "is-yes"
    if clinic["name"] in ("FONTANA CLINIC Tenjin", "Mirai Medical Clinic Setagaya"):
        return "대응 안내", "is-yes"
    return "미확인", "is-unknown"


def korean_note(clinic):
    notes = {
        "Japan Net Clinic": "공식 페이지는 한국인 의사가 한국어·영어·일본어로 진료한다고 적습니다. 원장 외 직원의 국적과 상주 여부는 확인되지 않았습니다.",
        "FONTANA CLINIC Tenjin": "공식 페이지는 한국어 대응 스태프가 매일 있다고 적습니다. 직원의 국적은 확인되지 않았습니다.",
        "Mirai Medical Clinic Setagaya": "공식 페이지는 예약·진료·사후 상담을 한국어로 진행한다고 적습니다. 직원 국적은 확인되지 않았습니다.",
        "MIL CLINIC OSAKA": "공식 페이지의 온라인 진료 언어 안내는 일본어·영어입니다. 한국어 진료 안내는 확인되지 않았습니다.",
    }
    return notes.get(clinic["name"], "한국어 진료 가능 여부는 공식 안내에서 확인되지 않음")


def english_status(clinic):
    if clinic["name"] in ("Nihonbashi Clinic", "MIL CLINIC OSAKA", "Japan Net Clinic"):
        return "확인", "is-yes"
    if clinic["name"] == "Shinbashi Ginza Swift Clinic":
        return "영문 페이지", "is-mid"
    return "미확인", "is-unknown"


def online_status(clinic):
    if "온라인" in clinic["summary"] + clinic["booking"]:
        return "확인", "is-yes"
    return "미확인", "is-unknown"


def card(clinic):
    pills = "".join(
        [
            ext(clinic["mounjaro"], "공식 마운자로 안내", "pill"),
            ext(clinic["access"], "공식 연락처·오시는 길", "pill"),
        ]
    )
    actions = "".join(ext(url, label, "pill") for url, label in clinic["links"])
    korea = clinic.get("korea_consult", "한국 거주자 상담 가능 여부는 공식 안내에서 확인되지 않음")
    checked = CHECKED.get(clinic["name"], "2026-11-11")
    city_name = CITY_NAME[clinic["city"]]
    search = " ".join([clinic["name"], clinic["jp"], clinic["area"], city_name, clinic["summary"]])
    korea_value, korea_kind = korea_status(clinic)
    english_value, english_kind = english_status(clinic)
    online_value, online_kind = online_status(clinic)
    hours_note = ""
    if "다르" in clinic["hours"]:
        hours_note = '<p class="hours-flag">공식 페이지와 예약 화면의 시간 표기가 다릅니다. 아래 상세에 출처별로 적었습니다.</p>'
    line = line_details() if has_line(clinic) else ""
    return f"""
        <article class="clinic-card" id="{e(clinic['city'])}-{e(clinic['name'].lower().replace(' ', '-'))}" data-city="{e(clinic['city'])}" data-search="{e(search)}">
          <div class="clinic-top">
            <h4 class="clinic-name">{e(clinic['name'])}<small>{e(clinic['jp'])}</small></h4>
            <span class="area-pill">{e(clinic['area'])}</span>
          </div>
          <ul class="compare">
            {status_item("온라인 상담 안내", online_value, online_kind)}
            {status_item("한국 체류 중 상담", korea_value, korea_kind)}
            {status_item("한국어 진료", korean_status(clinic)[0], korean_status(clinic)[1])}
            {status_item("영어 상담", english_value, english_kind)}
          </ul>
          {hours_note}
          <p class="clinic-summary">{e(clinic['summary'])}</p>
          <p class="checked">확인일 {e(checked)} · 최신 내용은 공식 페이지에서 다시 확인하세요.</p>
          <details class="card-more">
            <summary>상세 정보 펼쳐보기</summary>
            <dl class="detail-list">
              {row("주소", e(clinic["address"]))}
              {row("전화", phone_html(clinic))}
              {row("이메일", e(clinic["email"]))}
              {row("운영시간", e(clinic["hours"]))}
              {row("진료 관련 안내", e(clinic["booking"]))}
              {row("한국에서 상담", e(korea))}
              {row("한국어 진료", e(korean_note(clinic)))}
              {row("확인일", e(checked))}
            </dl>
            <div class="pill-row">{pills}{actions}</div>
            {line}
            <div class="card-foot">{ext(map_url(clinic["address"]), "지도에서 위치 보기", "map-link")}</div>
          </details>
        </article>"""


def directory():
    parts = []
    nav = []
    for city_id, name, en in CITIES:
        group = [c for c in CLINICS if c["city"] == city_id]
        nav.append(f'<li><a href="#{city_id}" data-city-filter="{city_id}">{name} {len(group)}</a></li>')
        cards = "".join(card(c) for c in group)
        parts.append(
            f"""
      <section class="city-section" id="{city_id}" aria-labelledby="{city_id}-title">
        <div class="city-heading">
          <h3 id="{city_id}-title">{name}</h3>
          <span>{en} · {len(group)}곳</span>
        </div>
        <div class="clinic-grid">{cards}
        </div>
      </section>"""
        )
    return "\n".join(nav), "\n".join(parts)


def map_section():
    boxes = []
    for city_id, name, _en in CITIES:
        group = [c for c in CLINICS if c["city"] == city_id]
        rows = []
        for clinic in group:
            rows.append(
                f"""<div class="map-row"><div><strong>{e(clinic['name'])}</strong><span>{e(clinic['address'])}</span></div>{ext(map_url(clinic['address']), "지도에서 위치 보기", "map-link")}</div>"""
            )
        boxes.append(
            f'<section class="map-city" aria-label="{e(name)} 주소"><h3>{name} · {len(group)}곳</h3>{"".join(rows)}</section>'
        )
    return "\n".join(boxes)


def head(title, description, path):
    url = f"{SITE_URL}{path}"
    return f"""<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#111111">
  <meta name="description" content="{e(description)}">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <title>{e(title)}</title>
  <link rel="canonical" href="{e(url)}">
  <link rel="icon" href="/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="/styles.css?v=9">
  <link rel="sitemap" type="application/xml" href="/sitemap.xml">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="ko_KR">
  <meta property="og:site_name" content="{SITE_NAME}">
  <meta property="og:title" content="{e(title)}">
  <meta property="og:description" content="{e(description)}">
  <meta property="og:url" content="{e(url)}">
  <meta name="twitter:card" content="summary">
  <meta name="twitter:title" content="{e(title)}">
  <meta name="twitter:description" content="{e(description)}">
  <!-- SITE_URL: YOUR_PUBLIC_SITE_URL 을 실제 주소로 바꾸세요. index.html, support.html, robots.txt, sitemap.xml -->
"""


INDEX_DESC = "도쿄·오사카·후쿠오카·삿포로·나고야·교토·지바의 의료기관이 공개한 마운자로 온라인 상담 정보와 연락처를 정리한 독립 정보 디렉터리입니다. 한국 체류 중 상담 가능 여부는 각 기관 공식 페이지의 문구를 옮겼습니다."
SUPPORT_DESC = "이 안내가 도움이 되셨다면 개발자에게 커피 한 잔 사주세요."


def build_index():
    nav, sections = directory()
    chips = ['<button class="chip" type="button" data-city-filter="all" aria-pressed="true">전체</button>']
    for city_id, name, _en in CITIES:
        count = sum(1 for clinic in CLINICS if clinic["city"] == city_id)
        chips.append(
            f'<button class="chip" type="button" data-city-filter="{city_id}" aria-pressed="false">{e(name)} {count}</button>'
        )
    chip_html = "\n".join(chips)
    html = head(f"{SITE_NAME} | 일본 공개 진료 정보", INDEX_DESC, "/")
    html += f"""  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "WebPage",
    "name": "{SITE_NAME}",
    "inLanguage": "ko",
    "isAccessibleForFree": true,
    "url": "{SITE_URL}/",
    "description": "{INDEX_DESC}"
  }}
  </script>
</head>
<body>
  <a class="skip" href="#directory">도시별 목록으로 건너뛰기</a>
  <header class="topbar">
    <div class="wrap nav">
      <a class="brand" href="/"><span class="brand-mark" aria-hidden="true">원</span><span>{SITE_NAME}</span></a>
      <nav aria-label="주요 메뉴">
        <ul class="nav-links">
          <li><a href="#directory">도시별 목록</a></li>
          <li><a href="#korean">한국어 진료</a></li>
          <li><a href="#line-guide">문의 문장</a></li>
          <li><a href="#safety">안전 안내</a></li>
          <li><a href="#sources">출처</a></li>
          <li><a class="meal-nav" href="/support.html"><span class="meal-emoji" aria-hidden="true">☕</span> 커피 한 잔</a></li>
        </ul>
      </nav>
    </div>
  </header>
  <main id="top">
    <section class="hero" aria-labelledby="page-title">
      <div class="wrap hero-grid">
        <div>
          <p class="eyebrow">일본 공개 진료 정보를 모은 목록</p>
          <h1 id="page-title">{SITE_NAME}</h1>
          <p class="hero-copy">공식 페이지에 공개된 마운자로 온라인 상담 정보와 연락처를 도시별로 모았습니다. 상담과 처방은 의료진 판단에 달려 있습니다. 이 사이트는 일본 의료기관의 공식 웹사이트, 광고, 제휴 서비스가 아닌 독립 정보 안내입니다.</p>
          <form class="finder" role="search">
            <label for="clinic-search">기관 찾기</label>
            <input id="clinic-search" type="search" placeholder="기관명, 일본어 이름, 지역" autocomplete="off">
          </form>
          <div class="chip-row" role="group" aria-label="도시 선택">
            {chip_html}
          </div>
          <ul class="stat-row">
            <li><strong>{len(CITIES)}</strong><span>도시</span></li>
            <li><strong>{len(CLINICS)}</strong><span>기관</span></li>
            <li><strong>공식</strong><span>자료 기준</span></li>
          </ul>
          <p class="microcopy">독립 정보 안내 · 의료기관과 비제휴 · 광고 없음 · 진료·예약 대행 없음</p>
        </div>
        <aside class="hero-panel" aria-label="한국 이용자에게 중요한 사항">
          <h2>이용 전 확인하세요</h2>
          <div class="panel-row"><span class="panel-mark" aria-hidden="true">?</span><span><strong>한국에서 온라인 상담이 가능한지</strong><br>HANI CLINIC, FONTANA CLINIC Tenjin, 세타가야 Mirai Medical Clinic 공식 페이지에는 한국에 있을 때의 상담 안내가 있습니다. MIL CLINIC OSAKA는 출발 전 상담을 안내합니다. 한국어로 진료한다는 안내와는 별개이며, 나머지 기관은 확인되지 않았습니다.</span></div>
          <div class="panel-row"><span class="panel-mark" aria-hidden="true">!</span><span><strong>한국으로 약을 보내는 직구</strong><br>식품의약품안전처와 관세청은 우편·특송 직접구매를 허용하지 않는다고 밝혔습니다. 2026년 11월 12일부터 허용된 것은 본인이 휴대해 들어오는 경우입니다.</span></div>
          <div class="panel-row"><span class="panel-mark" aria-hidden="true">!</span><span><strong>처방이 보장되는지</strong><br>아닙니다. 의료진의 진찰·판단 후 처방되지 않을 수 있습니다.</span></div>
        </aside>
      </div>
    </section>
    <div class="notice-band">
      <div class="wrap notice-inner">
        <span class="notice-icon" aria-hidden="true">!</span>
        <p><strong>의료·법률 안내.</strong> 이 페이지는 의료기관이 아니며 진료·예약·처방·의약품 판매·배송을 제공하지 않고, 개인정보나 건강정보를 수집하지 않습니다. 외부 링크는 각 기관의 공식 페이지 또는 공식 예약·문의 채널로 이동합니다. 한국 보건복지부 자료는 비의료인이 특정 의료기관의 위치·연락처·진료시간 등을 상세히 게시해 내원을 유도하는 유형에 의료광고상 쟁점이 있을 수 있다고 설명합니다. 이 페이지의 법적 분류는 확정되지 않았으므로 공개·운영 전 국내 법률 검토가 필요합니다. 최신 정보는 각 기관의 공식 페이지에서 확인하세요.</p>
      </div>
    </div>
    <section id="directory">
      <div class="wrap">
        <div class="section-head">
          <div>
            <p class="section-kicker">공식 페이지 공개 정보</p>
            <h2>도시별 의료기관 안내</h2>
          </div>
          <p class="section-intro">공식 페이지에 마운자로 상담 안내와 공개 연락 경로가 있는 곳을 담았습니다. 나열 순서는 자료를 정리한 순서이며 순위가 아닙니다. 주소와 운영시간은 카드를 펼치면 나옵니다. 지도 링크도 그 안에 있습니다.</p>
        </div>
        <p id="filter-empty" hidden>해당하는 기관이 없습니다.</p>
        <nav aria-label="도시 바로가기"><ul class="city-nav">{nav}</ul></nav>
        {sections}
      </div>
    </section>
    <section id="korean">
      <div class="wrap">
        <div class="section-head">
          <div>
            <p class="section-kicker">조건은 서로 다릅니다</p>
            <h2>한국어 진료와 한국 체류 중 상담</h2>
          </div>
          <p class="section-intro">한국어로 응대할 수 있다는 안내와, 한국에 있는 상태에서 원격 진료를 할 수 있다는 안내는 다른 내용입니다. 아래는 2026년 11월 12일에 각 기관 공식 페이지에서 확인한 문장만 나눕니다.</p>
        </div>
        <div class="three-cards">
          <article class="info-card">
            <span class="number">01</span>
            <h3>한국 체류 중 상담</h3>
            <p>한국에 있는 동안 일본 의료기관과 원격으로 상담할 수 있다고 공식 페이지에 적힌 곳입니다.</p>
            <p><a href="#chiba-hani-clinic">HANI CLINIC</a> · <a href="#fukuoka-fontana-clinic-tenjin">FONTANA CLINIC Tenjin</a> · <a href="#tokyo-mirai-medical-clinic-setagaya">Mirai Medical Clinic Setagaya</a></p>
            <p>MIL CLINIC OSAKA는 일본 비거주자의 출발 전 상담을 안내합니다. 한국 거주만 한정한 문장은 없고, 안내된 언어는 일본어·영어입니다.</p>
          </article>
          <article class="info-card">
            <span class="number">02</span>
            <h3>일본 현지 한국어 진료</h3>
            <p>일본에서 한국어로 진료·상담한다고 적힌 곳입니다. 한국에 있는 동안 진료할 수 있다는 뜻은 아닙니다.</p>
            <p><a href="#tokyo-japan-net-clinic">Japan Net Clinic</a>은 한국인 의사가 진료한다고 적혀 있습니다. 확인된 여행객 답변은 일본 체류 중 진료이고, 해외 배송은 제공하지 않는다고 적혀 있습니다.</p>
            <p><a href="#fukuoka-fontana-clinic-tenjin">FONTANA CLINIC Tenjin</a>과 <a href="#tokyo-mirai-medical-clinic-setagaya">세타가야 Mirai</a>도 한국어 대응을 안내합니다.</p>
          </article>
          <article class="info-card">
            <span class="number">03</span>
            <h3>한국인 직원 상주</h3>
            <p>공개된 공식 정보만으로는 직원 국적과 상주 여부를 확정한 곳이 없습니다. Japan Net Clinic은 진료하는 의사가 한국인이라고 적혀 있고, FONTANA는 한국어 대응 스태프가 매일 있다고 적혀 있습니다.</p>
          </article>
        </div>
        <div class="note-list">
          <article class="info-card">
            <h3>GLOBE Clinic Shinjuku</h3>
            <p>공식 한국어 페이지는 일본을 방문한 외국인·재일 외국인·호텔 투숙객을 대상으로 한국어 온라인 진료를 안내하고, 의사와 의료 통역 스태프가 연계한다고 적습니다. 한국에 있는 환자의 진료 가능 문장은 확인되지 않았고, 마운자로 처방 안내도 확인되지 않았습니다. 통역 스태프의 국적은 확인되지 않았습니다.</p>
            <p>〒160-0022 東京都新宿区新宿3丁目28番4号 TRES SHINJUKU 3階 · +81-3-5990-2471 · 공식 사이트 기준 매일 9:00–13:00, 15:00–19:00.</p>
            <p><a href="https://www.globe-clinic.jp/kr/telemedicine/" target="_blank" rel="noopener noreferrer">한국어 온라인 진료 페이지</a></p>
          </article>
          <article class="info-card">
            <h3>TOKYO IBIKI CLINIC INTERNATIONAL</h3>
            <p>공식 한국어 페이지는 관광객 진료, 호텔 왕진, 영어·중국어·한국어 대응을 안내합니다. 한국에서의 원격 진료 가능 여부는 확인되지 않았습니다. 비만·당뇨병 외래는 안내되어 있으나 마운자로라는 이름은 확인되지 않았습니다. 담당자 국적과 상주 여부는 확인되지 않았습니다.</p>
            <p>〒160-0022 東京都新宿区新宿3-22-11 RSビル10F · +81-3-6457-7375 · tokyoibiki@gmail.com. 진료 안내는 11:00–20:00이고 목요일 휴진이라고 적혀 있습니다. 같은 페이지의 다른 문구는 연중무휴 11:00–20:00이라고도 적습니다.</p>
            <p><a href="https://international-tokyo.com/ko/" target="_blank" rel="noopener noreferrer">한국어 진료 안내</a></p>
          </article>
        </div>
        <p class="phrase-disclaimer">후쿠오카 Mirai Medical Clinic(miraimedical.com)과 세타가야 Mirai Medical Clinic(mirai-medical.clinic)은 다른 기관입니다. 도쿄도 보건의료국의 외국인 환자 언어 지원 목록은 마운자로 처방이나 한국 체류 중 상담을 확인해 주는 자료가 아니므로 이 목록에 넣지 않았습니다.</p>
      </div>
    </section>
    <section id="line-guide">
      <div class="wrap">
        <div class="section-head">
          <div>
            <p class="section-kicker">문의 문장 예시</p>
            <h2>LINE 문의 문장 가이드</h2>
          </div>
          <p class="section-intro">일본어로 공식 채널에 확인할 때 참고하는 표현입니다. 상담을 신청하는 문구가 아니며, 어느 기관이 가능하다고 알려 주는 답변도 아닙니다.</p>
        </div>
        <div class="phrase-list">
          {phrase_items()}
        </div>
        <p class="phrase-disclaimer">위 문장은 일반적인 문의 표현의 예시이며, 특정 의료기관의 공식 답변이나 상담 가능 여부를 의미하지 않습니다. 실제 진료·처방 가능 여부는 해당 기관에 확인해야 합니다.</p>
      </div>
    </section>
    <section id="safety">
      <div class="wrap">
        <div class="section-head">
          <div>
            <p class="section-kicker">한국 이용 관련 안내</p>
            <h2>상담과 처방은 서로 다른 문제입니다.</h2>
          </div>
          <p class="section-intro">일본 의료기관의 온라인 진료 정보를 봤다는 사실만으로 한국에서 이용할 수 있거나 약을 국내로 반입할 수 있다고 볼 수 없습니다.</p>
        </div>
        <div class="three-cards">
          <article class="info-card"><span class="number">01</span><h3>한국에서 상담 가능한가요?</h3><p>한국어 응대와 한국에 있는 상태의 원격 진료는 다른 조건입니다. HANI CLINIC, FONTANA CLINIC Tenjin, 세타가야 Mirai Medical Clinic의 공식 페이지는 한국에 있을 때의 상담을 안내하고, MIL CLINIC OSAKA는 출발 전 상담을 안내합니다. Japan Net Clinic은 한국어 진료를 안내하지만, 확인된 답변은 일본 체류 중 진료입니다. 그 문장은 해당 카드와 한국어 진료 메뉴에 옮겼습니다.</p></article>
          <article class="info-card"><span class="number">02</span><h3>처방을 받을 수 있나요?</h3><p>보장되지 않습니다. 의사는 온라인 진료가 적절하지 않다고 판단하면 진료를 중단하거나 대면 진료를 안내할 수 있고, 처방하지 않을 수도 있습니다.</p></article>
          <article class="info-card"><span class="number">03</span><h3>한국으로 보내도 되나요?</h3><p>우편이나 특송으로 받는 직접구매는 허용되지 않습니다. 식약처·관세청은 2026년 11월 12일부터 해외에서 정상적으로 처방·구매한 자가 치료용 의약품을 본인이 휴대 반입하는 경우만 수량 한도 안에서 허용한다고 밝혔습니다. <a href="https://www.yna.co.kr/view/AKR20261111158151017" target="_blank" rel="noopener noreferrer">연합뉴스 보도</a> · <a href="https://www.mfds.go.kr/brd/m_99/view.do?seq=50487" target="_blank" rel="noopener noreferrer">식약처 보도자료</a></p></article>
        </div>
        <div class="safety">
          <p class="section-kicker">의약품 안전 안내</p>
          <h2>마운자로는 처방의약품입니다.</h2>
          <p>일본 후생노동성은 제2형 당뇨병 치료제가 미용·체중감량 목적으로 사용될 때 안전성과 유효성이 확인되지 않았다고 경고합니다. 이 페이지는 사용이나 체중감량을 권하지 않으며 의료 조언을 대신하지 않습니다. <a href="https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/kenkou_iryou/iyakuhin/kojinyunyu/index_00003.html" target="_blank" rel="noopener noreferrer">일본 후생노동성 안전 안내</a></p>
        </div>
      </div>
    </section>
    <section class="sources-section" id="sources">
      <div class="wrap">
        <div class="section-head">
          <div>
            <p class="section-kicker">공식 자료·검토 근거</p>
            <h2>공식 원문 자료</h2>
          </div>
          <p class="section-intro">법률 관련 자료는 이 안내의 적법성을 확정하는 법률 의견이 아닙니다.</p>
        </div>
        <div class="source-list">
          <a class="source" href="https://www.mhlw.go.jp/stf/seisakunitsuite/bunya/kenkou_iryou/iyakuhin/kojinyunyu/index_00003.html" target="_blank" rel="noopener noreferrer"><small>일본 후생노동성 · MHLW</small><strong>마운자로 등 당뇨병 치료제 안전 안내</strong><span>미용·체중감량 목적 사용의 안전성과 유효성이 확인되지 않았다는 공식 안내</span></a>
          <a class="source" href="https://www.mhlw.go.jp/stf/newpage_38226.html" target="_blank" rel="noopener noreferrer"><small>일본 후생노동성 · MHLW</small><strong>온라인 진료 이용 시 환자 안내</strong><span>온라인 진료가 모든 환자에게 가능한 것은 아니며, 의사가 처방하지 않을 수 있다는 안내</span></a>
          <a class="source" href="https://www.mohw.go.kr/board.es?mid=a10503010100&amp;bid=0027&amp;act=view&amp;list_no=371102&amp;tag=&amp;nPage=140" target="_blank" rel="noopener noreferrer"><small>대한민국 보건복지부 · 2022년 보도자료</small><strong>치료경험담 등 불법 의료광고 모니터링</strong><span>비의료인 게시물의 의료기관 상세 정보·내원 유도 표현 관련 쟁점을 다룹니다. 법적 분류는 확정되지 않았습니다.</span></a>
          <a class="source" href="https://www.yna.co.kr/view/AKR20261111158151017" target="_blank" rel="noopener noreferrer"><small>연합뉴스 · 2026년 11월 11일</small><strong>외국에서 구매한 비만약 휴대 반입, 직구는 불가</strong><span>식약처·관세청 발표를 전하며, 휴대 반입과 달리 의약품 직접구매는 인정되지 않는다고 적습니다.</span></a>
          <a class="source" href="https://www.mfds.go.kr/brd/m_99/view.do?seq=50487" target="_blank" rel="noopener noreferrer"><small>식품의약품안전처 · 2026년 11월 11일</small><strong>자가 치료용 의약품 개인 휴대 반입 허용 보도자료</strong><span>관세청과 함께 낸 휴대 반입 안내입니다. 우편·특송 직접구매 허용 발표는 아닙니다.</span></a>
        </div>
      </div>
    </section>
  </main>
  <footer class="site-footer">
    <div class="wrap">
      <section class="legal-cushion" aria-labelledby="legal-cushion-title">
        <h2 id="legal-cushion-title">법적 유의사항</h2>
        <p>본 페이지는 각 기관이 공개한 자료를 모은 독립 정보 안내입니다. 의료기관이 아니고, 법률 자문이나 행정기관의 공식 해석도 아닙니다. 진료·처방·예약·의약품 판매를 하지 않으며, 특정 기관을 권하거나 순위를 매기지 않습니다.</p>
        <p>수록 정보는 실시간으로 바뀔 수 있고, 공식 페이지의 현재 내용과 다를 수 있습니다. 상담·처방 가능 여부와 법령의 적용은 각 기관과 관계 당국의 공식 안내에서 확인해야 합니다. 이 페이지를 보고 한 판단과 그 결과는 이용자 본인에게 있습니다. 이 문구는 법적 책임을 면하게 해 주는 법률 의견이 아닙니다.</p>
      </section>
      <p class="tip-line"><span aria-hidden="true">📬</span> <strong>제보</strong> 틀린 곳이나 바뀐 내용이 있으면 알려 주세요. <a href="mailto:moonblind@daum.net">moonblind@daum.net</a></p>
      <div class="footer-inner">
        <p>독립 정보 안내 · 의료기관과 비제휴 · 광고 없음 · 법적 분류는 확정되지 않음</p>
        <p><a href="/support.html"><span class="meal-emoji" aria-hidden="true">☕</span> 개발자에게 커피 한 잔</a> · 공식 자료 확인 기준: 2026년 11월 11일 · 의료 조언이 아닙니다.</p>
      </div>
    </div>
  </footer>
  <a class="meal-side" href="/support.html"><span class="meal-emoji" aria-hidden="true">☕</span><span class="meal-label">커피 한 잔</span></a>
  <script src="/filter.js?v=2"></script>
  <script src="/copy.js"></script>
</body>
</html>
"""
    return html


def build_support():
    html = head(f"개발자에게 커피 한 잔 | {SITE_NAME}", SUPPORT_DESC, "/support.html")
    html += f"""</head>
<body>
  <a class="skip" href="#support-title">본문으로 건너뛰기</a>
  <header class="topbar">
    <div class="wrap nav">
      <a class="brand" href="/"><span class="brand-mark" aria-hidden="true">원</span><span>{SITE_NAME}</span></a>
      <a class="button ghost" href="/">정보 목록으로</a>
    </div>
  </header>
  <main class="support-main">
    <section class="support-card" aria-labelledby="support-title">
      <p class="eyebrow">별도 페이지</p>
      <h1 id="support-title"><span class="meal-emoji" aria-hidden="true">☕</span>개발자에게 커피 한 잔</h1>
      <p class="message">이 안내가 도움이 되셨다면 개발자에게 커피 한 잔 사주세요.</p>
      <div class="account" aria-label="계좌 안내">
        <div class="account-row"><span class="account-label">은행</span><span class="account-value">토스뱅크</span></div>
        <div class="account-row"><span class="account-label">계좌번호</span><span class="account-value account-number" id="account-number">1002-0836-8104</span></div>
        <div class="phrase-actions">
          <button class="copy-button" type="button" id="copy-account" data-copy="1002-0836-8104" data-copied="계좌번호를 복사했습니다.">계좌번호 복사</button>
          <p class="copy-status" id="copy-status" data-copy-status role="status" aria-live="polite"></p>
        </div>
      </div>
      <p class="footnote">이 페이지는 의료기관 정보와 별도로 운영됩니다.</p>
    </section>
  </main>
  <footer class="site-footer">
    <div class="wrap">
      <section class="legal-cushion" aria-labelledby="support-legal-title">
        <h2 id="support-legal-title">법적 유의사항</h2>
        <p>이 페이지의 계좌 안내는 의료기관 정보와 별개입니다. 본 사이트는 법률 자문이 아니며, 수록 정보는 실시간으로 바뀔 수 있습니다. 이 문구는 법적 책임을 면하게 해 주는 법률 의견이 아닙니다.</p>
      </section>
      <p class="tip-line"><span aria-hidden="true">📬</span> <strong>제보</strong> 틀린 곳이나 바뀐 내용이 있으면 알려 주세요. <a href="mailto:moonblind@daum.net">moonblind@daum.net</a></p>
      <p><a href="/">{SITE_NAME}로 돌아가기</a></p>
    </div>
  </footer>
  <script src="/copy.js"></script>
</body>
</html>
"""
    return html


def build_404():
    return """<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="robots" content="noindex">
  <title>페이지를 찾을 수 없습니다 | 마운자로 원정대</title>
  <link rel="stylesheet" href="/styles.css?v=9">
</head>
<body>
  <main class="missing">
    <p class="eyebrow">404</p>
    <h1>페이지를 찾을 수 없습니다.</h1>
    <p><a class="button primary" href="/">정보 목록으로</a></p>
  </main>
</body>
</html>
"""


def main():
    if len(CLINICS) != 23:
        raise SystemExit(f"expected 21 clinics, got {len(CLINICS)}")
    (ROOT / "index.html").write_text(build_index(), encoding="utf-8")
    (ROOT / "support.html").write_text(build_support(), encoding="utf-8")
    (ROOT / "404.html").write_text(build_404(), encoding="utf-8")
    (ROOT / "robots.txt").write_text(
        "\n".join(
            [
                "User-agent: *",
                "Allow: /",
                "",
                f"Sitemap: {SITE_URL}/sitemap.xml",
                "",
                "# 다음 웹마스터도구 인증 코드는 발급받은 뒤 이 줄 아래에 그대로 붙이세요.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    (ROOT / "sitemap.xml").write_text(
        f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>{SITE_URL}/</loc>
    <lastmod>2026-11-12</lastmod>
  </url>
  <url>
    <loc>{SITE_URL}/support.html</loc>
    <lastmod>2026-11-12</lastmod>
  </url>
</urlset>
""",
        encoding="utf-8",
    )
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    count = html.count('class="clinic-card"')
    if count != 23:
        raise SystemExit(f"rendered {count} cards")
    print("wrote", count, "clinics")


if __name__ == "__main__":
    main()
