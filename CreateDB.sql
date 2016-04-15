CREATE TABLE Subreddit (
    name VARCHAR(24) NOT NULL,
    banner_link VARCHAR(24),
    logo_link VARCHAR(24),
    users_online VARCHAR(24),
    PRIMARY KEY (name)
);
           
CREATE TABLE User (
    username VARCHAR(24) NOT NULL,
    link_karma INTEGER,
    comment_karma INTEGER,
    PRIMARY KEY (username)
);

CREATE TABLE Post (
    post_id INTEGER NOT NULL,
    title VARCHAR(120),
    post_type VARCHAR(120),
    subreddit VARCHAR(24) NOT NULL,
    username VARCHAR(120) NOT NULL,
    stacked BOOLEAN,
    gilded BOOLEAN,
    upvotes INTEGER,
    PRIMARY KEY (post_id),
    FOREIGN KEY (subreddit)
        REFERENCES Subreddit (name),
    FOREIGN KEY (username)
        REFERENCES User (username)
);

CREATE TABLE Comment (
    comment_id INTEGER NOT NULL,
    post_id INTEGER NOT NULL,
    username VARCHAR(120) NOT NULL,
    gilded BOOLEAN,
    upvotes INTEGER,
    text VARCHAR(1000),
    PRIMARY KEY (comment_id),
    FOREIGN KEY (post_id)
        REFERENCES Post (post_id),
    FOREIGN KEY (username)
        REFERENCES User (username)
);


CREATE TABLE Trophy (
    trophy_id INTEGER NOT NULL,
    name VARCHAR(24),
    icon VARCHAR(200),
    PRIMARY KEY (trophy_id)
);

CREATE TABLE Subscribes (
    username INTEGER NOT NULL,
    subreddit VARCHAR(24) NOT NULL,
    PRIMARY KEY (username , subreddit),
    FOREIGN KEY (username)
        REFERENCES User (username),
    FOREIGN KEY (subreddit)
        REFERENCES Subreddit (name)
);

CREATE TABLE UserTrophies (
    username INTEGER NOT NULL,
    trophy_id INTEGER NOT NULL,
    PRIMARY KEY (username , trophy_id),
    FOREIGN KEY (username)
        REFERENCES User (username),
    FOREIGN KEY (trophy_id)
        REFERENCES Trophy (trophy_id)
);


CREATE TABLE Moderator (
    username INTEGER NOT NULL,
    subreddit VARCHAR(24) NOT NULL,
    PRIMARY KEY (username , subreddit),
    FOREIGN KEY (username)
        REFERENCES User (username),
    FOREIGN KEY (subreddit)
        REFERENCES Subreddit (name)
);
