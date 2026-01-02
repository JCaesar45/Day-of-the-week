function findXmasSunday(startYear, endYear) {
    const sundayYears = [];
    
    for (let year = startYear; year <= endYear; year++) {
        // Create date for December 25th of current year
        const xmasDate = new Date(year, 11, 25); // Month is 0-indexed, so 11 = December
        
        // Check if December 25th is a Sunday (0 = Sunday, 1 = Monday, etc.)
        if (xmasDate.getDay() === 0) {
            sundayYears.push(year);
        }
    }
    
    return sundayYears;
}
