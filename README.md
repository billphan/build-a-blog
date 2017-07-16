# build-a-blog
LC101 assignment

This small, flask-based app implements a blog.

## Entity Analysis

* A _blog_ is a series of _entries_
* Each _entry_ includes a _title_ and a _body_

## Requirements

The app must meet several requirements:

* List all previous blog entries in chronological order
* List all previous blog entries in reverse-chronological order
* Allow anybody to create a new blog entry
* Display the individual blog entry after creation
* Include a menu bar with available commands

### Non-requirements

* No authentication or authorization is required
* All access can be anonymous

## User Scenarios

### Scenario 0 : Default display
* **Given** I am an anonymous visitor to the site
* **When** I arrive at the site (route "/")
* **Then** I see a list of previous blog entries in oldest-first order

### Scenario 1 : Menu available all the time
* **Given** I am an anonymous visitor 
* **When** on any page
* **Then** I can see a menu of actions available to me

### Scenario 2 : Reverse chronological order display
* **Given** I am an anonymous visitor
* **When** on any page
* **And** I click on the "List all entries (newest-first)" menu item
* **Then** I see a list of previous blog entries in newest-first order

### Scenario 3 : Chronological order display
* **Given** I am an anonymous visitor
* **When** on any page
* **And** I click on the "List all entries (oldest-first)" menu item
* **Then** I see a list of previous blog entries in oldest-first order

### Scenario 4 : Create new entry form display
* **Given** I am an anonymous visitor
* **When** I click on the "Create new entry" menu items
* **Then** I go to the "Create new entry" form page
* **And** I see a form for entering a title and a body

### Scenario 5 : Successfully create new entry
* **Given** I am an anonymous visitor 
* **And** I am on the "Create new entry" form page
* **When** I supply a _title_
* **And** I supply a _body_
* **And** I click the "Save" button
* **Then** I see my new entry on a page by itself

### Scenario 6 : Create new entry with errors
* **Given** I am an anonymous visitor 
* **And** I am on the "Create new entry" form page
* **When** I DO NOT supply a title
* **Or** I DO NOT supply a body
* **And** I click the "Save" button
* **Then** I see the same form with my given values (if any) for _title_ and _body_ with an error message


## User accessible command (the menu items):
* List all entries (oldest-first)
* List all entries (newest-first)
* Create new entry

## Routes

* **"/"** - GET: redirect to "/blog"
* **"/blog"** - GET: Display list of all entries with default sort order (oldest-first)
* **"/blog?sort=newest"** - GET: Display list of all entries newest-first
* **"/blog?sort=oldest"** - GET: Display list of all entries oldest-first
* **"/blog?id=#"** GET: Display entry with id=ID
* **"/post"** - GET: Display new entry form; POST: Process new entry
