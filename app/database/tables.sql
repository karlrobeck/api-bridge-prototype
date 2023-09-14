CREATE TABLE StudentBalance (
    student_id not null int,
    user_id not null int,
    title not null text,
    current_balance not null float,
    date_issued not null varchar(255),
    date_expiry not null varchar(255),
    prelim not null float,
    midterms not null float,
    prefinals not null float,
    finals not null float
)