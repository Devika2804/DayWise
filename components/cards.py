

import streamlit as st


def section_title(title: str):
    st.markdown(f"## {title}")


def metric_card(title: str, value: str, subtitle: str = ""):
    st.markdown(
        f'''
<div style="
border:1px solid #e5e7eb;
border-radius:16px;
padding:20px;
background:white;
min-height:180px;">
<h3>{title}</h3>
<h1 style="margin-bottom:0;">{value}</h1>
<p style="color:#6b7280;">{subtitle}</p>
</div>
''',
        unsafe_allow_html=True,
    )


def info_card(title: str, body: str):
    st.markdown(
        f'''
<div style="
border:1px solid #e5e7eb;
border-radius:16px;
padding:20px;
background:white;
min-height:180px;">
<h3>{title}</h3>
<p style="font-size:17px;line-height:1.8;">
{body}
</p>
</div>
''',
        unsafe_allow_html=True,
    )


def list_card(title: str, items):
    html = "<br>".join(items)

    st.markdown(
        f'''
<div style="
border:1px solid #e5e7eb;
border-radius:16px;
padding:20px;
background:white;
min-height:180px;">
<h3>{title}</h3>
<p style="font-size:18px;line-height:2;">
{html}
</p>
</div>
''',
        unsafe_allow_html=True,
    )


def hero_card(title: str, text: str):
    st.markdown(
        f'''
<div style="
background:#f8fbff;
border:1px solid #dbeafe;
border-radius:16px;
padding:24px;
margin-bottom:20px;">
<h2>{title}</h2>
<p style="font-size:20px;line-height:1.8;">
{text}
</p>
</div>
''',
        unsafe_allow_html=True,
    )
