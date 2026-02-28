INSERT INTO "public"."buildings" ("id", "address", "lat", "lon") VALUES
('468d8e52-b6b8-41b9-91de-769bd85b7181', 'г. Москва, ул. Ленина 1, офис 3', 55.7558, 37.6173),
('6a52dab1-615c-4247-b5cb-c9149c549250', 'г. Новосибирск, ул. Блюхера 32/1', 54.9893, 82.8991),
('8995e058-45bf-4351-b8fe-984baed7fbe7', 'г. Санкт-Петербург, Невский проспект 10', 59.9360, 30.3146);



INSERT INTO "public"."activities" ("id", "name", "level") VALUES
('a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11', 'Еда', 0),
('a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a12', 'Автомобили', 0),
('a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a13', 'Мясная продукция', 1),
('a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a14', 'Молочная продукция', 1),
('a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a15', 'Легковые', 1),
('a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a16', 'Запчасти', 2),
('a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a17', 'Аксессуары', 2);



INSERT INTO "public"."organizations" ("id", "name", "building_id", "activity_id") VALUES
('f47ac10b-58cc-4372-a567-0e02b2c3d471', 'ООО Рога и Копыта', '6a52dab1-615c-4247-b5cb-c9149c549250', 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a13'),
('f47ac10b-58cc-4372-a567-0e02b2c3d472', 'АвтоМир', '468d8e52-b6b8-41b9-91de-769bd85b7181', 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a16'),
('f47ac10b-58cc-4372-a567-0e02b2c3d473', 'Молочный Рай', '8995e058-45bf-4351-b8fe-984baed7fbe7', 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a14');


INSERT INTO "public"."phones" ("id", "number", "organization_id") VALUES
(gen_random_uuid(), '2-222-222', 'f47ac10b-58cc-4372-a567-0e02b2c3d471'),
(gen_random_uuid(), '3-333-333', 'f47ac10b-58cc-4372-a567-0e02b2c3d471'),
(gen_random_uuid(), '8-923-666-13-13', 'f47ac10b-58cc-4372-a567-0e02b2c3d471'),
(gen_random_uuid(), '8-800-555-35-35', 'f47ac10b-58cc-4372-a567-0e02b2c3d472');


INSERT INTO "public"."activitytree" ("id", "parent_id", "child_id") VALUES
('a0eebc99-9c0b-4ef8-bb6d-6bb9bd480a17', 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11', 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a13'),
('a0eebc99-9c0b-4ef8-bb6d-6bb9bd480a27', 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11', 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a14'),
('a0eebc99-9c0b-4ef8-bb6d-6bb9bd480a37', 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a12', 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a15'),
('a0eebc99-9c0b-4ef8-bb6d-6bb9bd480a47', 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a15', 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a16'),
('a0eebc99-9c0b-4ef8-bb6d-6bb9bd480a57', 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a15', 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a17');
