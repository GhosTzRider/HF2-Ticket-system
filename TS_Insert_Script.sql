INSERT INTO users (first_name, last_name, email)
VALUES 
('Marcus', 'Odense', 'marcus@odense.dk'),
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

INSERT INTO supporters (first_name, last_name, email)
VALUES
('Oliver', 'Munkebo', 'oliver@support.dk'),
('Mads','Kerteminde','mads@support.dk'),
('Nico','Haarby','nico@support.dk'),
('Noah','København','noah@support.dk'),
('Frode','Korup','frode@support.dk');

INSERT INTO acticles (title, content, category_id, supporter_id, created_at, updated_at)
VALUES
('How to fix login issues',
 'If you cannot log in, try resetting your password and clearing browser cache.',
 4, 1, GETDATE(), GETDATE()),

('Troubleshooting slow computer',
 'Restart your device, check for background processes, and ensure updates are installed.',
 2, 2, GETDATE(), GETDATE()),

('Fixing network connectivity',
 'Check your router, restart it, and verify cables are connected properly.',
 3, 3, GETDATE(), GETDATE()),

('Installing new software',
 'Download the installer from the official website and follow the installation guide.',
 1, 4, GETDATE(), GETDATE()),

('General IT support tips',
 'Always keep your system updated and avoid suspicious downloads.',
 5, 5, GETDATE(), GETDATE()),

('Password reset guide',
 'Use the "Forgot Password" feature and follow the instructions sent to your email.',
 4, 2, GETDATE(), GETDATE()),

('Fix printer not working',
 'Check printer connection, drivers, and restart the print spooler service.',
 2, 1, GETDATE(), GETDATE());


INSERT INTO tickets 
(title, description, user_id, category_id, service_id, priority_id, status_id, supporter_id, created_at, updated_at)
VALUES
('Cannot log into account',
 'User reports login failure after password change.',
 1, 4, 4, 3, 1, 1, GETDATE(), GETDATE()),

('Computer is very slow',
 'System takes too long to boot and open applications.',
 2, 2, 1, 2, 2, 2, GETDATE(), GETDATE()),

('Internet not working',
 'No connection to the company network since morning.',
 3, 3, 3, 4, 1, 3, GETDATE(), GETDATE()),

('Software installation error',
 'Error appears during installation of internal tool.',
 4, 1, 2, 3, 2, 4, GETDATE(), GETDATE()),

('Forgot password',
 'User unable to access account and needs reset.',
 5, 4, 4, 2, 3, 2, GETDATE(), GETDATE()),

('Printer not responding',
 'Printer does not print even though it is connected.',
 1, 2, 1, 1, 1, 5, GETDATE(), GETDATE()),

('VPN connection drops',
 'VPN disconnects every 10 minutes.',
 2, 3, 3, 4, 2, 3, GETDATE(), GETDATE()),

('Email not syncing',
 'Emails are not updating in Outlook.',
 3, 1, 2, 2, 2, 1, GETDATE(), GETDATE()),

('Account locked',
 'Too many failed login attempts caused lockout.',
 4, 4, 4, 3, 3, 4, GETDATE(), GETDATE()),

('Other issue',
 'User reports unspecified issue requiring investigation.',
 5, 5, 5, 1, 1, NULL, GETDATE(), GETDATE());


INSERT INTO ticket_comments (ticket_id, supporter_id, user_id, comment, created_at)
VALUES
(1, 1, 1, 'We are currently investigating your login issue.', GETDATE()),
(1, 1, 1, 'Please try resetting your password again and let us know.', GETDATE()),

(2, 2, 2, 'Have you tried restarting your computer?', GETDATE()),
(2, 2, 2, 'We recommend checking for background processes.', GETDATE()),

(3, 3, 3, 'Network team has been notified.', GETDATE()),
(3, 3, 3, 'Please confirm if the issue still persists.', GETDATE()),

(4, 4, 4, 'Installation error noted, checking logs.', GETDATE()),
(4, 4, 4, 'Try reinstalling with admin privileges.', GETDATE()),

(5, 2, 5, 'Password reset instructions have been sent.', GETDATE()),
(5, 2, 5, 'Let us know if you did not receive the email.', GETDATE()),

(6, 5, 1, 'Printer connection looks fine, checking drivers.', GETDATE()),
(6, 5, 1, 'Please restart the printer and try again.', GETDATE()),

(7, 3, 2, 'VPN instability confirmed, working on fix.', GETDATE()),
(7, 3, 2, 'Temporary workaround: reconnect manually.', GETDATE()),

(8, 1, 3, 'Email sync issue under investigation.', GETDATE()),
(8, 1, 3, 'Try refreshing Outlook manually.', GETDATE()),

(9, 4, 4, 'Account has been unlocked.', GETDATE()),
(9, 4, 4, 'Please use a stronger password next time.', GETDATE()),

(10, 5, 5, 'We need more details about your issue.', GETDATE()),
(10, 5, 5, 'Please provide screenshots if possible.', GETDATE());

DELETE FROM ticket_comments;