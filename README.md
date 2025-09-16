# DatabaseDesign_MovieRoundTable
## Project Overview

This project is a Film Information Management System built on IMDb’s open dataset (with additional data from Douban Top250). It provides a comprehensive platform for users, film professionals, and administrators to browse, query, evaluate, and manage film-related information.

## Background & Objectives
	-	Users: Access film and crew information, perform personalized queries, manage watch history, and share evaluations.
	-	Film Professionals: Upload and update film records, track audience feedback.
	-	Administrators: Manage users, content, and system security, ensuring accuracy and reliability.

The system is implemented with a three-tier architecture (data layer, business logic layer, presentation layer), using MySQL + Django, and supports multilingual titles, cross-platform access, and secure permission control.

## Key Features

1. User Features:
   - Registration, login, and password recovery
   - Browse and query films and actors
	-	Rate and review films
	-	Manage watchlist (mark films as “watched”)

3. Advanced User Features: 
	-	Upload and edit their own film records
	-	Maintain film-related metadata
	-	Interact with the community through reviews and ratings

4. Administrator Features: 
	-	Admin registration & login
	-	Review and approve user/film submissions
	-	Manage users (CRUD operations)
	-	Manage categories and film tags
	-	Moderate user comments and content

## Database Design

	-	Core Entities: Film personnel, films, crew, episodes, alternative titles, ratings, users, user reviews
	-	Key Relationships:
	-	User ↔ Film (reviews, ratings, watchlist marks)
	-	Film Personnel ↔ Film (director, writer, actor roles)

The schema was designed with normalization up to BCNF, ensuring integrity, flexibility, and efficiency. Optimizations include separating region-language data and indexing on primary keys.

## Implementation
	-	Backend: Django framework connected to MySQL
	-	Data Sources: IMDb dataset (daily updated) + Douban Top250 (via web crawler)
	-	Frontend:
	-	User-friendly interfaces for login, film/actor search, and personal profile management
	-	Film detail pages with ratings, comments, and links to external resources
	-	Admin dashboard for content and user management
