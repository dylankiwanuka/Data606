#What Are joins
-used to combine matched rows from two or more tables
-e.g rows from nultiple tables: joins are how we combine rows from two or more tables of matching data and create a new table.
-insert image 1

type of join is decided by what you want back

#Types of JOIN

##Inner JOIN

-most common is Inner Join : middle of venn diagram
-essentially intersection the common things in two tables 


##Left JOIN

-gives you evrything from the left table and the matched / in common rows from the right table 

##Right JOIN

-guves you eveyrthing from the Right table and the macthed rows from the right table.

##Full Join
-Retuns all rows from both tables

-need a column that is present in both tables

-examples:

SELECT Customers.CompanyName, Orders.OrderID, Orders.OrderDate
FROM Customers 
INNER JOIN Orders o ON Customers.CustomerID = Orders.CustomerID;

SELECT o.OrderID, p.ProductName, od.Quantity
FROM Orders o
INNER JOIN [Order Details ] od
    ON o.OrderID = od.OrderID
INNER JOIN Products p
    ON od.ProductID = p.ProductID;

SELECT o.OrderID, SUM(od.Quantity * od.UnitPrice) AS OrderTotal
FROM Orders o
INNER JOIN [Order Details] od 
    ON o.OrderID = od.OrderID
GROUP BY o.OrderID;

SELECT c.CompanyName
FROM Customers c
LEFT JOIN Orders o
    ON c.CustomerID = o.CustomerID
WHERE o.OrderID IS NULL;

SELECT p.ProductName
FROM Products p
LEFT JOIN [Order Details] od
    ON p.ProductID = od.ProductID
WHERE od.ProductID IS NULL;

-Multi Dimensional
-Left Joins are often used to find NULLs