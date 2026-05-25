# Technical Decisions

## Backend Framework
Used Django REST Framework because:
- Fast API development
- Built-in ORM
- Easy serializer support
- Good admin panel

## Frontend Framework
Used React with Vite because:
- Fast development
- Component-based structure
- Easy API integration

## Database
Used SQLite for simplicity and fast setup.

## File Upload
Used multipart/form-data for CSV upload handling.

## Suspicious Record Detection
Implemented simple business rules:
- Negative fuel values
- High electricity usage
- High travel distance

## Deployment Choice
- Backend deployed using Render
- Frontend deployed using Vercel

These platforms provide easy GitHub integration and free hosting.