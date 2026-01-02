import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

# PALETTE DE COULEURS je vais me baser sur mon site web https://nicolasherve4.github.io/Site_Nicolas/landing_page/

# la palette de couleurs
ACCENT_NEON = "#B2FF2B"  
ACCENT_MEDIUM = "#2500F6"
ACCENT_DARK = "#FB0505"
BG_DARK = "#000000"
BG_SURFACE = "#070D15"
TEXT_SECONDARY = "#52607C"

# Palette pour graphiques multiples
COLOR_PALETTE = [ACCENT_NEON, ACCENT_MEDIUM, ACCENT_DARK, "#3B0D89", "#1F2A3D", "#8EB2E8", "#FF6F61", "#22692B"]

px.defaults.template = "plotly_dark"
px.defaults.color_continuous_scale = COLOR_PALETTE
px.defaults.color_discrete_sequence = COLOR_PALETTE

# Créer un template personnalisé
pio.templates["nicolas_herve"] = go.layout.Template(
    layout=go.Layout(
        font=dict(family="Arial", size=14, color="#FFFFFF"),
        title=dict(font=dict(size=24, color=COLOR_PALETTE[0])),
        xaxis=dict(
            title_font=dict(size=16, color="#26D420"),
            gridcolor=TEXT_SECONDARY,
            gridwidth=0.5
        ),
        yaxis=dict(
            title_font=dict(size=16, color="#26D420"),
            gridcolor=TEXT_SECONDARY,
            gridwidth=0.5
        ),
        legend=dict(
            font=dict(size=14, color="#FFFFFF"),
            title_font=dict(size=16)
        ),
        paper_bgcolor=BG_DARK,
        plot_bgcolor=BG_SURFACE,
        colorway=COLOR_PALETTE
    )
)
