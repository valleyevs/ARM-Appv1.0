import streamlit as st

# --- COMPLETE REFERENCE RANGES (System & Gender Specific) ---
REFERENCE_RANGES = {
    # --- DEMOGRAPHICS & ANATOMY ---
    "Average Anal Canal Length (cm)": {
        "Solid-State HRAM": {
            "Female": {"poor_low": 1.5, "normal_min": 2.3, "normal_max": 5.0, "poor_high": 6.0},
            "Male":   {"poor_low": 2.0, "normal_min": 3.0, "normal_max": 5.5, "poor_high": 6.5}
        },
        "Water-Perfused": {
            "Female": {"poor_low": 1.5, "normal_min": 2.5, "normal_max": 4.0, "poor_high": 5.0},
            "Male":   {"poor_low": 2.0, "normal_min": 3.0, "normal_max": 4.5, "poor_high": 5.5}
        }
    },
    
    # --- COUGH REFLEX (Resting Tone & Reflex) ---
    "Resting Min (mmHg)": {
        "Solid-State HRAM": {
            "Female": {"normal_min": 30, "normal_max": 80},
            "Male":   {"normal_min": 40, "normal_max": 100}
        }
    },
    "Resting Mean (mmHg)": {
        "Solid-State HRAM": {
            "Female": {"poor_low": 30, "normal_min": 50, "normal_max": 90, "poor_high": 120},
            "Male":   {"poor_low": 40, "normal_min": 60, "normal_max": 110, "poor_high": 140}
        }
    },
    "Resting 5th (mmHg)": {
        "Solid-State HRAM": {
            "Female": {"normal_min": 40, "normal_max": 80},
            "Male":   {"normal_min": 50, "normal_max": 95}
        }
    },
    "Resting Max (mmHg)": {
        "Solid-State HRAM": {
            "Female": {"normal_min": 60, "normal_max": 110},
            "Male":   {"normal_min": 70, "normal_max": 130}
        }
    },
    "Cough Box Mean (mmHg)": {
        "Solid-State HRAM": {
            "Female": {"poor_low": 40, "normal_min": 60, "normal_max": 150},
            "Male":   {"poor_low": 50, "normal_min": 70, "normal_max": 180}
        }
    },
    "Cough Box Max (mmHg)": {
        "Solid-State HRAM": {
            "Female": {"poor_low": 50, "normal_min": 70, "normal_max": 200},
            "Male":   {"poor_low": 60, "normal_min": 80, "normal_max": 250}
        }
    },

    # --- SQUEEZE ASSESSMENT ---
    "Average Squeeze Mean (mmHg)": {
        "Solid-State HRAM": {
            "Female": {"poor_low": 40, "normal_min": 60, "normal_max": 200, "poor_high": 300},
            "Male":   {"poor_low": 60, "normal_min": 90, "normal_max": 250, "poor_high": 350}
        }
    },
    "Squeeze Max (mmHg)": {
        "Solid-State HRAM": {
            "Female": {"poor_low": 50, "normal_min": 80, "normal_max": 250, "poor_high": 350},
            "Male":   {"poor_low": 70, "normal_min": 110, "normal_max": 300, "poor_high": 400}
        }
    },
    "Squeeze Duration (sec)": {
        "Solid-State HRAM": {
            "Female": {"poor_low": 5, "normal_min": 10, "normal_max": 40, "poor_high": 60},
            "Male":   {"poor_low": 5, "normal_min": 10, "normal_max": 40, "poor_high": 60}
        }
    },
    "Endurance Mean (mmHg)": {
        "Solid-State HRAM": {
            "Female": {"poor_low": 30, "normal_min": 50, "normal_max": 180},
            "Male":   {"poor_low": 50, "normal_min": 70, "normal_max": 200}
        }
    },
    "Endurance Max (mmHg)": {
        "Solid-State HRAM": {
            "Female": {"poor_low": 40, "normal_min": 70, "normal_max": 250},
            "Male":   {"poor_low": 60, "normal_min": 100, "normal_max": 300}
        }
    },
    "Endurance Duration (sec)": {
        "Solid-State HRAM": {
            "Female": {"poor_low": 10, "normal_min": 20, "normal_max": 60},
            "Male":   {"poor_low": 10, "normal_min": 20, "normal_max": 60}
        }
    },

    # --- PUSH MANEUVER ---
    "Push Resting Mean (mmHg)": {
        "Solid-State HRAM": {
            "Female": {"poor_low": 30, "normal_min": 50, "normal_max": 90, "poor_high": 120},
            "Male":   {"poor_low": 40, "normal_min": 60, "normal_max": 110, "poor_high": 140}
        }
    },
    "Rectal Resting Mean (mmHg)": {
        "Solid-State HRAM": {
            "Female": {"normal_min": 5, "normal_max": 25, "poor_high": 40},
            "Male":   {"normal_min": 5, "normal_max": 25, "poor_high": 40}
        }
    },
    "Push Residual Pressure (mmHg)": {
        "Solid-State HRAM": {
            "Female": {"poor_low": 0, "normal_min": 10, "normal_max": 45, "poor_high": 80},
            "Male":   {"poor_low": 0, "normal_min": 10, "normal_max": 45, "poor_high": 80}
        }
    },
    "Push Relaxation (%)": {
        "Solid-State HRAM": {
            "Female": {"poor_low": 0, "normal_min": 20, "normal_max": 100, "poor_high": 101},
            "Male":   {"poor_low": 0, "normal_min": 20, "normal_max": 100, "poor_high": 101}
        }
    },
    "Rectal Exp. Inc Mean (mmHg)": {
        "Solid-State HRAM": {
            "Female": {"poor_low": 10, "normal_min": 30, "normal_max": 100},
            "Male":   {"poor_low": 15, "normal_min": 35, "normal_max": 100}
        }
    },
    "Rectal Exp. Inc Max (mmHg)": {
        "Solid-State HRAM": {
            "Female": {"poor_low": 15, "normal_min": 40, "normal_max": 150},
            "Male":   {"poor_low": 20, "normal_min": 45, "normal_max": 150}
        }
    },

    # --- RAIR & SENSATION ---
    "RAIR Resting Min (mmHg)": {
        "Solid-State HRAM": {
            "Female": {"normal_min": 30, "normal_max": 80},
            "Male":   {"normal_min": 40, "normal_max": 100}
        }
    },
    "RAIR Resting Mean (mmHg)": {
        "Solid-State HRAM": {
            "Female": {"normal_min": 50, "normal_max": 90},
            "Male":   {"normal_min": 60, "normal_max": 110}
        }
    },
    "RAIR Resting 5th (mmHg)": {
        "Solid-State HRAM": {
            "Female": {"normal_min": 40, "normal_max": 80},
            "Male":   {"normal_min": 50, "normal_max": 95}
        }
    },
    "RAIR Resting Max (mmHg)": {
        "Solid-State HRAM": {
            "Female": {"normal_min": 60, "normal_max": 110},
            "Male":   {"normal_min": 70, "normal_max": 130}
        }
    },
    "RAIR Volume (ml)": {
        "Solid-State HRAM": {
            "Female": {"poor_low": 0, "normal_min": 10, "normal_max": 50, "poor_high": 80},
            "Male":   {"poor_low": 0, "normal_min": 10, "normal_max": 50, "poor_high": 80}
        }
    },
    "RAIR Residual (mmHg)": {
        "Solid-State HRAM": {
            "Female": {"normal_min": 0, "normal_max": 40, "poor_high": 60},
            "Male":   {"normal_min": 0, "normal_max": 45, "poor_high": 65}
        }
    },
    "RAIR Relaxation (%)": {
        "Solid-State HRAM": {
            "Female": {"poor_low": 10, "normal_min": 25, "normal_max": 100, "poor_high": 101},
            "Male":   {"poor_low": 10, "normal_min": 25, "normal_max": 100, "poor_high": 101}
        }
    },
    "RAIR Duration (sec)": {
        "Solid-State HRAM": {
            "Female": {"poor_low": 2, "normal_min": 5, "normal_max": 30, "poor_high": 45},
            "Male":   {"poor_low": 2, "normal_min": 5, "normal_max": 30, "poor_high": 45}
        }
    },
    "First Sensation (ml)": {
        "Solid-State HRAM": {
            "Female": {"poor_low": 5, "normal_min": 15, "normal_max": 40, "poor_high": 80},
            "Male":   {"poor_low": 5, "normal_min": 15, "normal_max": 40, "poor_high": 80}
        }
    },
    "First Urge Volume (ml)": {
        "Solid-State HRAM": {
            "Female": {"poor_low": 10, "normal_min": 30, "normal_max": 90, "poor_high": 150},
            "Male":   {"poor_low": 15, "normal_min": 35, "normal_max": 100, "poor_high": 160}
        }
    },
    "Max Tolerable (ml)": {
        "Solid-State HRAM": {
            "Female": {"poor_low": 50, "normal_min": 100, "normal_max": 250, "poor_high": 400},
            "Male":   {"poor_low": 60, "normal_min": 110, "normal_max": 280, "poor_high": 450}
        }
    }
}

st.set_page_config(page_title="Anorectal Manometry Clinical Tool", layout="wide")
st.title("Anorectal Manometry Clinical Tool")

# --- INITIALIZE SESSION STATE FOR INPUTS ---
if 'inputs' not in st.session_state:
    st.session_state.inputs = {}

# --- DEMOGRAPHICS TOP BAR ---
col1, col2, col3 = st.columns(3)
with col1:
    system = st.selectbox("System Type", ["Solid-State HRAM", "Water-Perfused"])
with col2:
    gender = st.selectbox("Gender", ["Female", "Male"])
with col3:
    indication = st.selectbox("Indication", [
        "Constipation/Obstructed defecation", "Faecal Incontinence", "Anorectal Pain", 
        "Pre op assessment (fistula surgery, sphincter repair etc)", "Post partum assessment", 
        "Biofeedback Training", "Other"
    ])
    
age = st.number_input("Age", min_value=0, max_value=120, value=0, step=1)
acl = st.number_input("Average Anal Canal Length (cm)", min_value=0.0, max_value=10.0, value=0.0, step=0.1)
st.session_state.inputs["Average Anal Canal Length (cm)"] = acl

# --- HELPER FUNCTIONS ---
def evaluate_value(field, val, sys, gen):
    if val == 0.0 or val is None:
        return ""
    if field in REFERENCE_RANGES and sys in REFERENCE_RANGES[field]:
        ranges = REFERENCE_RANGES[field][sys].get(gen)
        if not ranges:
            return ""
        if val < ranges.get("poor_low", float('-inf')):
            return "🔴 Poor (Critically Low)"
        elif val < ranges.get("normal_min", float('-inf')):
            return "🟡 Low"
        elif val > ranges.get("poor_high", float('inf')):
            return "🔴 Poor (Critically High)"
        elif val > ranges.get("normal_max", float('inf')):
            return "🔵 High"
        else:
            return "🟢 Normal"
    return ""

def render_field(field_name):
    ranges_str = "Norms pending"
    if field_name in REFERENCE_RANGES and system in REFERENCE_RANGES[field_name]:
        ranges = REFERENCE_RANGES[field_name][system].get(gender)
        if ranges:
            n_min = ranges.get("normal_min", "")
            n_max = ranges.get("normal_max", "")
            ranges_str = f"Normal: {n_min} - {n_max}"
            
    val = st.number_input(f"{field_name} ({ranges_str})", min_value=0.0, value=0.0, step=0.1, key=field_name)
    st.session_state.inputs[field_name] = val
    status = evaluate_value(field_name, val, system, gender)
    if status:
        st.markdown(f"**Status:** {status}")
    st.divider()

# --- TABS ---
tab_names = ["Squeeze", "Cough Reflex", "Push Maneuver", "RAIR & Sensation", "Final Interpretation", "References"]
tabs = st.tabs(tab_names)

sections = {
    "Squeeze": [
        "Average Squeeze Mean (mmHg)", "Squeeze Max (mmHg)", "Squeeze Duration (sec)",
        "Endurance Mean (mmHg)", "Endurance Max (mmHg)", "Endurance Duration (sec)"
    ],
    "Cough Reflex": [
        "Resting Min (mmHg)", "Resting Mean (mmHg)", "Resting 5th (mmHg)", "Resting Max (mmHg)",
        "Cough Box Mean (mmHg)", "Cough Box Max (mmHg)"
    ],
    "Push Maneuver": [
        "Push Resting Mean (mmHg)", "Rectal Resting Mean (mmHg)",
        "Push Residual Pressure (mmHg)", "Push Relaxation (%)", 
        "Rectal Exp. Inc Mean (mmHg)", "Rectal Exp. Inc Max (mmHg)"
    ],
    "RAIR & Sensation": [
        "RAIR Resting Min (mmHg)", "RAIR Resting Mean (mmHg)", "RAIR Resting 5th (mmHg)", "RAIR Resting Max (mmHg)",
        "RAIR Volume (ml)", "RAIR Residual (mmHg)", "RAIR Relaxation (%)", "RAIR Duration (sec)",
        "First Sensation (ml)", "First Urge Volume (ml)", "Max Tolerable (ml)"
    ]
}

for i, section_name in enumerate(["Squeeze", "Cough Reflex", "Push Maneuver", "RAIR & Sensation"]):
    with tabs[i]:
        for field in sections[section_name]:
            render_field(field)

# --- FINAL INTERPRETATION TAB ---
with tabs[4]:
    st.subheader("Generate Clinical Summary")
    bet = st.selectbox("Balloon Expulsion Test (BET)", ["Not Performed", "Normal", "Prolonged/Abnormal"])
    
    if st.button("Generate London Classification Report", type="primary"):
        report = []
        report.append(f"**INDICATION:** {indication}")
        report.append(f"**SYSTEM:** {system} | **GENDER:** {gender}")
        report.append("---")
        
        def get_val(field):
            val = st.session_state.inputs.get(field, 0.0)
            return val if val != 0.0 else None
            
        def get_limits(field):
            if field in REFERENCE_RANGES and system in REFERENCE_RANGES[field]:
                return REFERENCE_RANGES[field][system].get(gender, {})
            return {}

        # 1. Anal Tone & Contractility
        resting_mean = get_val("Resting Mean (mmHg)")
        resting_limits = get_limits("Resting Mean (mmHg)")
        squeeze_max = get_val("Squeeze Max (mmHg)")
        squeeze_limits = get_limits("Squeeze Max (mmHg)")
        
        tone_diagnosis = "Normal anal tone and contractility."
        is_hypo_tone = resting_mean is not None and resting_limits and resting_mean < resting_limits.get("normal_min", 0)
        is_hyper_tone = resting_mean is not None and resting_limits and resting_mean > resting_limits.get("normal_max", 999)
        is_hypo_contractile = squeeze_max is not None and squeeze_limits and squeeze_max < squeeze_limits.get("normal_min", 0)
        
        if is_hypo_tone and is_hypo_contractile:
            tone_diagnosis = "Combined anal hypotension and hypocontractility."
        elif is_hypo_tone:
            tone_diagnosis = "Anal hypotension with normal contractility."
        elif is_hyper_tone:
            tone_diagnosis = "Anal hypertension."
        elif is_hypo_contractile:
            tone_diagnosis = "Anal normotension with hypocontractility."
            
        report.append(f"**TONE & CONTRACTILITY:** {tone_diagnosis}")

        # 2. RAIR
        rair_relax = get_val("RAIR Relaxation (%)")
        rair_limits = get_limits("RAIR Relaxation (%)")
        if rair_relax is not None and rair_limits:
            if rair_relax < rair_limits.get("normal_min", 25):
                report.append("**RAIR:** Rectoanal areflexia (Reflex not elicited).")
            else:
                report.append("**RAIR:** Present and normal.")
                
        # 3. Sensation
        fcsv = get_val("First Sensation (ml)")
        ddv = get_val("First Urge Volume (ml)")
        mtv = get_val("Max Tolerable (ml)")
        
        sensory_high_count = 0
        sensory_low_count = 0
        
        for val, field in [(fcsv, "First Sensation (ml)"), (ddv, "First Urge Volume (ml)"), (mtv, "Max Tolerable (ml)")]:
            limits = get_limits(field)
            if val is not None and limits:
                if val > limits.get("normal_max", 999): sensory_high_count += 1
                if val < limits.get("normal_min", 0): sensory_low_count += 1
                
        if sensory_high_count >= 2:
            report.append("**SENSATION:** Rectal hyposensitivity.")
        elif sensory_high_count == 1:
            report.append("**SENSATION:** Borderline rectal hyposensitivity.")
        elif sensory_low_count >= 1:
            report.append("**SENSATION:** Rectal hypersensitivity.")
        else:
            if fcsv and ddv and mtv:
                report.append("**SENSATION:** Normal rectal sensation.")
                
        # 4. Coordination
        if bet == "Not Performed":
            report.append("**COORDINATION:** Inconclusive (Balloon Expulsion Test not performed).")
        else:
            push_relax = get_val("Push Relaxation (%)")
            push_relax_limits = get_limits("Push Relaxation (%)")
            rectal_inc = get_val("Rectal Exp. Inc Max (mmHg)")
            rectal_inc_limits = get_limits("Rectal Exp. Inc Max (mmHg)")
            
            is_dyssynergic = push_relax is not None and push_relax_limits and push_relax < push_relax_limits.get("normal_min", 20)
            is_poor_propulsion = rectal_inc is not None and rectal_inc_limits and rectal_inc < rectal_inc_limits.get("normal_min", 40)
            
            if bet == "Prolonged/Abnormal":
                if is_dyssynergic and is_poor_propulsion:
                    report.append("**COORDINATION:** Abnormal expulsion with poor propulsion and dyssynergia.")
                elif is_dyssynergic:
                    report.append("**COORDINATION:** Abnormal expulsion with dyssynergia.")
                elif is_poor_propulsion:
                    report.append("**COORDINATION:** Abnormal expulsion with poor propulsion.")
                else:
                    report.append("**COORDINATION:** Abnormal expulsion with normal manometric pattern.")
            elif bet == "Normal":
                if is_dyssynergic or is_poor_propulsion:
                    report.append("**COORDINATION:** Normal expulsion with abnormal manometric pattern.")
                else:
                    report.append("**COORDINATION:** Normal manometric pattern with normal expulsion.")

        for line in report:
            st.write(line)

# --- REFERENCES TAB ---
with tabs[5]:
    st.subheader("References & Normative Data Sources")
    st.markdown("[1. The London Classification: Improving Characterization and Classification of Anorectal Function with Anorectal Manometry (Scott & Carrington, 2020).](https://doi.org/10.1007/s11894-020-00793-z)")
    st.markdown("[2. The international anorectal physiology working group (IAPWG) recommendations: Standardized testing protocol and the London classification (Carrington et al., 2019).](https://doi.org/10.1111/nmo.13679)")
    st.markdown("[3. Traditional measures of normal anal sphincter function using high-resolution anorectal manometry (HRAM) in 115 healthy volunteers (Carrington et al., 2014).](https://doi.org/10.1111/nmo.12307)")
    st.markdown("[4. High-resolution anorectal manometry: a comparison of solid-state and water-perfused catheters (Rasijeff et al., 2017).](https://doi.org/10.1111/nmo.13124)")

# --- GLOBAL DISCLAIMER ---
st.markdown("---")
st.caption("*(This is simply a tool to display what is abnormal on manometry reports and clinical decision making rests with the physician interpreting it)*")