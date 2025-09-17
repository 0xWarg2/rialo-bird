# Supabase Leaderboard API Contract

**Feature**: 001-title-rialo-bird  
**Date**: 2025-01-27  
**Status**: Complete

## Base URL
```
https://drsyehmbsoofjdhtivdf.supabase.co/rest/v1
```

## Authentication
- **Type**: Anonymous (RLS enabled)
- **Headers**: 
  - `apikey: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRyc3llaG1ic29vZmpkaHRpdmRmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTgwODA4NjEsImV4cCI6MjA3MzY1Njg2MX0.Z5R9KzkkUJL3bxjrFrse4lzziwJSbwG3SyI_caj9CCc`
  - `Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRyc3llaG1ic29vZmpkaHRpdmRmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTgwODA4NjEsImV4cCI6MjA3MzY1Njg2MX0.Z5R9KzkkUJL3bxjrFrse4lzziwJSbwG3SyI_caj9CCc`

## Endpoints

### GET /leaderboard
**Purpose**: Retrieve top scores for leaderboard display

**Query Parameters**:
- `order`: `score.desc` (required)
- `limit`: `10` (default: 10, max: 50)

**Example Request**:
```http
GET /leaderboard?order=score.desc&limit=10
apikey: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Success Response** (200):
```json
[
  {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "name": "Player1",
    "score": 42,
    "created_at": "2025-01-27T10:30:00Z"
  },
  {
    "id": "123e4567-e89b-12d3-a456-426614174001", 
    "name": "Player2",
    "score": 38,
    "created_at": "2025-01-27T09:15:00Z"
  }
]
```

**Error Responses**:
- `400 Bad Request`: Invalid query parameters
- `401 Unauthorized`: Invalid API key
- `429 Too Many Requests`: Rate limit exceeded
- `500 Internal Server Error`: Supabase backend error

### POST /leaderboard
**Purpose**: Submit new high score to leaderboard

**Request Body**:
```json
{
  "name": "PlayerName",
  "score": 42
}
```

**Validation Rules**:
- `name`: Required, 1-16 characters, alphanumeric + spaces only
- `score`: Required, integer 0-1,000,000

**Example Request**:
```http
POST /leaderboard
Content-Type: application/json
apikey: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

{
  "name": "Player1",
  "score": 42
}
```

**Success Response** (201):
```json
{
  "id": "123e4567-e89b-12d3-a456-426614174000",
  "name": "Player1", 
  "score": 42,
  "created_at": "2025-01-27T10:30:00Z"
}
```

**Error Responses**:
- `400 Bad Request`: Invalid request body or validation failure
- `401 Unauthorized`: Invalid API key
- `429 Too Many Requests`: Rate limit exceeded
- `500 Internal Server Error`: Supabase backend error

## Row Level Security (RLS) Policies

### Select Policy
```sql
CREATE POLICY "Allow anonymous read access" ON leaderboard
  FOR SELECT USING (true);
```

### Insert Policy  
```sql
CREATE POLICY "Allow anonymous insert with constraints" ON leaderboard
  FOR INSERT WITH CHECK (
    length(name) >= 1 AND 
    length(name) <= 16 AND
    score >= 0 AND 
    score <= 1000000
  );
```

## Rate Limiting
- **Anonymous users**: 10 requests per minute
- **Per IP**: 100 requests per hour
- **Burst allowance**: 5 requests per 10 seconds

## Error Handling

### Client-Side Error Handling
```python
async def submit_score(name: str, score: int) -> bool:
    try:
        response = await supabase.table('leaderboard').insert({
            'name': name,
            'score': score
        }).execute()
        return True
    except Exception as e:
        if e.code == 429:
            # Rate limited - retry later
            return False
        elif e.code == 400:
            # Validation error - fix input
            return False
        else:
            # Network/server error - graceful degradation
            return False
```

### Graceful Degradation
- Network failure → Store score locally only
- Rate limit → Queue for retry later
- Validation error → Show user-friendly message
- Server error → Fallback to local leaderboard

## Testing Strategy

### Contract Tests
- Test valid requests return expected responses
- Test invalid requests return appropriate errors
- Test rate limiting behavior
- Test RLS policy enforcement

### Integration Tests
- Test with real Supabase staging project
- Test anonymous authentication flow
- Test data persistence and retrieval
- Test error scenarios

### Performance Tests
- Test response times under load
- Test concurrent request handling
- Test rate limit recovery
- Test connection pooling
