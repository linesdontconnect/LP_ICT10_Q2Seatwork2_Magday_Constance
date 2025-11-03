from js import document

def compute_grade(event):
    try:
        # Use the event so the parameter is accessed (e.g. when called from a form)
        if event:
            event.preventDefault()

        # Get input values
        subjects = ["science", "english", "ict", "math", "filipino", "pe"]
        grades = []
        for subj in subjects:
            el = document.getElementById(subj)
            val = el.value if el is not None else ""
            try:
                grades.append(float(val) if val != "" else 0.0)
            except Exception:
                grades.append(0.0)

        # Compute average
        average = sum(grades) / len(grades) if grades else 0.0

        # Get student name
        first_el = document.getElementById("first")
        last_el = document.getElementById("last")
        first = first_el.value if first_el is not None else ""
        last = last_el.value if last_el is not None else ""

        # Display results by writing directly to DOM elements
        show1 = document.getElementById("show1")
        show2 = document.getElementById("show2")
        if show1 is not None:
            show1.innerText = f"Your  General Weighted Grade is:"
        if show2 is not None:
            show2.innerText = f"{average:.2f}"
    except Exception as e:
        show2 = document.getElementById("show2")
        if show2 is not None:
            show2.innerText = f"Error: {e}"
