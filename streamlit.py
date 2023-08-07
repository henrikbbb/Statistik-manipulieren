import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np

st.title('Statistiken manipulieren')

st.subheader('Aufgabe')
st.write('1. Ändere die Skalierung der Achsen, um mit dem entstehenden Diagramm einen gezielten Eindruck zu erzeugen.')
st.write('2. Erstelle eine reißerische Überschrift zu deinem Diagramm.')
st.write('3. Speichere das Diagramm unter dem Namen _Diagramm-Vorname.png_ ab und lade es bei IServ hoch.')
st.divider()

n = 20
x_values = list(x for x in range(20))
years = [2000 + x for x in x_values]
y_values = [2750 + y for y in [100, 105, 108, 110, 109, 108, 105, 102, 100, 90, 80, 70, 62, 60, 55, 50, 52, 45, 47, 50]]

x_min, x_max = st.select_slider(
    'Wähle die Zeitspanne aus.',
    options=years,
    value=(min(years), max(years))
)
x_min -= 2000
x_max -= 2000
# st.write('Du hast die Jahre', x_min, 'bis', x_max, 'ausgewählt.')

selected_x_values = list(range(x_min, x_max+1))
selected_y_values = [y_values[x] for x in selected_x_values]

y_min = st.slider(
    'Wähle den kleinsten y-Wert aus.',
    0,
    min(selected_y_values) - 1,
    0
)

y_max = st.slider(
    'Wähle den größten y-Wert aus.',
    max(selected_y_values),
    max(y_values)+1,
    max(y_values)+1
)

st.divider()

fig, ax = plt.subplots()
# plt.xticks(x_values)
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
ax.bar(years, y_values)
ax.set_xlabel('Jahr')
ax.set_ylabel('Gewinn in €')

x_min += 2000
x_max += 2000
ax.set_xlim(x_min - 0.5, x_max + 0.5)
ax.set_ylim(y_min, y_max + 1)

st.pyplot(fig)