import random
import flet as ft
import flet_charts as fch

def main(page: ft.Page):
    page.title = "Flet pie chart demo"

    sections = [
        fch.PieChartSection(value=40, title="40%", color=ft.Colors.BLUE, radius=80),
        fch.PieChartSection(value=30, title="30%", color=ft.Colors.YELLOW, radius=65),
        fch.PieChartSection(value=20, title="20%", color=ft.Colors.PINK, radius=60),
        fch.PieChartSection(value=10, title="10%", color=ft.Colors.GREEN, radius=70),
    ]

    def on_chart_event(e):
        if getattr(e, "section_index", None) is None:
            return
        idx = e.section_index
        section = chart.sections[idx]
        page.snack_bar = ft.SnackBar(ft.Text(f"{section.title}: {section.value}"))
        page.snack_bar.open = True
        page.update()

    chart = fch.PieChart(
        expand=True,
        sections_space=1,
        center_space_radius=30,
        sections=sections,
        on_event=on_chart_event,
    )

    def increase_blue(e):
        chart.sections[0].value += 5
        chart.update()

    def randomize(e):
        total = 100
        a = random.randint(5, 60)
        b = random.randint(5, total - a - 10)
        c = random.randint(5, total - a - b - 5)
        d = total - a - b - c
        chart.sections[0].value = a
        chart.sections[1].value = b
        chart.sections[2].value = c
        chart.sections[3].value = d
        chart.update()

    btn_increase = ft.ElevatedButton("Increase Blue", on_click=increase_blue)
    btn_random = ft.ElevatedButton("Randomize", on_click=randomize)

    controls = ft.Row([btn_increase, btn_random], spacing=20)

    page.add(controls, chart)

if __name__ == "__main__":
    ft.app(target=main)