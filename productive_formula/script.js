function calculateDiscipline() {
    // 1. Get raw input values or default to 0 if empty/invalid
    const work = parseFloat(document.getElementById('work').value) || 0;
    const exercise = parseFloat(document.getElementById('exercise').value) || 0;
    const timeWasted = parseFloat(document.getElementById('time_wasted').value) || 0;

    // 2. Perform the formula calculation: {[(work / 2) * exercise] - timeWasted}
    const result = ((work / 2) * exercise) - timeWasted;

    // 3. Update the formula span elements in the DOM
    document.getElementById('Points_of_work').textContent = work;
    document.getElementById('Points_of_Exercise').textContent = exercise;
    document.getElementById('Points_of_time_wasted').textContent = timeWasted;
    document.getElementById('Result').textContent = result;
}
