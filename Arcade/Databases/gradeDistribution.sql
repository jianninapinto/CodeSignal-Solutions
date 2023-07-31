CREATE PROCEDURE solution()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
	SELECT name, ID
	FROM Grades
	WHERE Final > (0.25 * (Midterm1 + Midterm2) + 0.5 * Final)
		OR Final > (0.5 * (Midterm1 + Midterm2))
	ORDER BY LEFT(Name, 3) ASC, ID ASC;
END