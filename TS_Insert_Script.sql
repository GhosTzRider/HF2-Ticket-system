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
('Reopen'),
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

INSERT INTO acticles (title, content, category_id, supporter_id)
VALUES
('Login Troubleshooting', 'Reset password and clear browser cache.', 4, 1),
('Fix Slow Computer', 'Remove unnecessary startup programs and scan for malware.', 2, 2),
('VPN Connection Guide', 'Ensure VPN client is updated and credentials are correct.', 3, 3),
('Email Not Syncing', 'Check server settings and internet connection.', 1, 4),
('Printer Not Working', 'Restart printer and reinstall drivers.', 2, 5),
('Account Locked', 'Too many failed attempts can lock your account.', 4, 1),
('Network Latency Issues', 'Check bandwidth usage and router placement.', 3, 2),
('Software Update Failed', 'Run update as administrator and disable antivirus temporarily.', 1, 3),
('Blue Screen Error', 'Check hardware drivers and system logs.', 2, 4),
('General IT Tips', 'Keep software updated and use strong passwords.', 5, 5);


INSERT INTO tickets (title, description, user_id, category_id, service_id, priority_id, status_id, supporter_id)
VALUES
('Login not working', 'Cannot login after password reset.', 1, 4, 4, 3, 1, 1),
('Laptop overheating', 'Device heats up quickly.', 2, 2, 1, 4, 3, 2),
('VPN not connecting', 'VPN fails to connect.', 3, 3, 3, 2, 2, 3),
('Email sync issue', 'Emails are not updating.', 4, 1, 2, 2, 1, 4),
('Printer offline', 'Printer shows offline status.', 5, 2, 1, 1, 4, 5),
('Account locked out', 'Too many failed login attempts.', 1, 4, 4, 3, 2, 1),
('Slow internet', 'Internet speed is very low.', 2, 3, 3, 2, 3, 2),
('App crashes', 'Application crashes on launch.', 3, 1, 2, 4, 1, 3),
('Blue screen error', 'System crashes with blue screen.', 4, 2, 1, 4, 3, 4),
('Access denied', 'Cannot access shared folder.', 5, 5, 4, 1, 4, 5);


INSERT INTO ticket_comments (ticket_id, supporter_id, user_id, comment)
VALUES
(1, 1, 1, 'Tried resetting password twice.'),
(1, 1, 1, 'Support sent a new reset link.'),
(2, 2, 2, 'Cleaned fan but still overheating.'),
(2, 2, 2, 'Check thermal paste.'),
(3, 3, 3, 'VPN error code 720 shown.'),
(3, 3, 3, 'Issue escalated to network team.'),
(4, 4, 4, 'Checked settings, still not syncing.'),
(4, 4, 4, 'Try removing and re-adding account.'),
(5, 5, 5, 'Restarted printer but no change.'),
(5, 5, 5, 'Driver reinstall fixed the issue.'),
(6, 1, 1, 'Account still locked after 24h.'),
(6, 1, 1, 'Unlocked manually by support.'),
(7, 2, 2, 'Speed drops during peak hours.'),
(7, 2, 2, 'Router firmware updated.'),
(8, 3, 3, 'Crash log attached.'),
(8, 3, 3, 'Reinstall resolved the issue.'),
(9, 4, 4, 'Blue screen error code 0x0001.'),
(9, 4, 4, 'Driver update fixed crash.'),
(10, 5, 5, 'Permission issue suspected.'),
(10, 5, 5, 'Access granted by admin.');
