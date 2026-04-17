INSERT INTO users (first_name, last_name, email)
VALUES 
('Marucs', 'Odense', 'marcus@odense.dk'),
('Philip', 'Vejle', 'philip@vejle.dk'),
('Mathias', 'Kolding', 'mathias@kolding.dk'),
('Rene', 'Haderselv', 'rene@haderselv.dk'),
('Mikkel', 'Korsør', 'mikkel@korsør.dk');

INSERT INTO categories (name)
VALUES 
('Software Issue'),
('Hardware Issue'),
('Network Issue'),
('Account Issue'),
('Other');

INSERT INTO services (name)
VALUES 
('IT Support'),
('Software Development'),
('Network Administration'),
('Account Management'),
('Other');

INSERT INTO priorities (name)
VALUES 
('Low'),
('Medium'),
('High'),
('Critical');

INSERT INTO statuses (name)
VALUES 
('Open'),
('In Progress'),
('Resolved'),
('Closed');