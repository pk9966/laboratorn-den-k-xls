76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
from difflib import SequenceMatcher

            if konstrukce and zkouska and stanice:
                total_count += count_matches_advanced(lab_df, konstrukce, zkouska, stanice)
        target_df.at[i, "D"] = total_count
        pozadovano = row.get("C")
        if pd.notna(pozadovano):
            target_df.at[i, "E"] = "Vyhovující" if total_count >= pozadovano else f"Chybí {abs(int(pozadovano - total_count))} zk."
    return target_df


def process_cely_objekt_sheet(key_df, target_df):
    for i, row in target_df.iterrows():
        material = row.get("materiál")
        zkouska = row.get("druh zkoušky")
        if pd.isna(material) or pd.isna(zkouska):
            continue
        count = count_matches_advanced(lab_df, material, zkouska, "")
        target_df.at[i, "C"] = count
        pozadovano = row.get("B")
        if pd.notna(pozadovano):
            target_df.at[i, "D"] = "Vyhovující" if count >= pozadovano else f"Chybí {abs(int(pozadovano - count))} zk."
    return target_df

if lab_file and xlsx_file:
    lab_bytes = lab_file.read()
    lab_df = pd.read_excel(io.BytesIO(lab_bytes), sheet_name="Evidence zkoušek zhotovitele")

    try:
        xlsx_bytes = xlsx_file.read()
        workbook = load_workbook(io.BytesIO(xlsx_bytes))

        def load_sheet_df(name):
            return pd.read_excel(io.BytesIO(xlsx_bytes), sheet_name=name)

        sheet_names = workbook.sheetnames

        def sheet_exists(name):
            return name in sheet_names

        op1_key = load_sheet_df("seznam zkoušek PM+LM OP1") if sheet_exists("seznam zkoušek PM+LM OP1") else pd.DataFrame()
        op2_key = load_sheet_df("seznam zkoušek PM+LM OP2") if sheet_exists("seznam zkoušek PM+LM OP2") else pd.DataFrame()
        cely_key = load_sheet_df("seznam zkoušek Celý objekt") if sheet_exists("seznam zkoušek Celý objekt") else pd.DataFrame()

        sheet_targets = [
            ("PM - OP1", op1_key),
            ("LM - OP1", op1_key),
            ("PM - OP2", op2_key),
            ("LM - OP2", op2_key),
            ("Celý objekt", cely_key),
        ]

        for sheet_name, key_df in sheet_targets:
            if sheet_exists(sheet_name) and not key_df.empty:
                df = load_sheet_df(sheet_name)
                processed = process_cely_objekt_sheet(key_df, df) if "Celý objekt" in sheet_name else process_op_sheet(key_df, df)
                ws = workbook[sheet_name]
                for i, row in processed.iterrows():
                    if "D" in processed.columns:
                        ws.cell(row=i+2, column=4, value=row.get("D"))
                    if "E" in processed.columns:
                        ws.cell(row=i+2, column=5, value=row.get("E"))

        output = io.BytesIO()
        workbook.save(output)

        st.success("Vyhodnocení dokončeno. Stáhni výsledný soubor níže.")
        st.download_button(
            label="📥 Stáhnout výsledný Excel",
            data=output.getvalue(),
            file_name="vyhodnoceni_vystup.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

    except Exception as e:
        st.error(f"Chyba při zpracování souboru: {e}")
