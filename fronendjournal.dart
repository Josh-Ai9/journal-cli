// A LOOK-ONLY Flutter demo of what your journal app's UI could become.
// No backend — entries are fake, hardcoded data just to show the shape.
// This is NOT wired to your Python journal.py yet.

import 'package:flutter/material.dart';

void main() => runApp(const JournalApp());

class JournalApp extends StatelessWidget {
  const JournalApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'My Journal',
      theme: ThemeData(useMaterial3: true, colorSchemeSeed: Colors.teal),
      home: const EntryListScreen(),
    );
  }
}

// --- Fake data, just standing in for what your journal.json holds ---
class Entry {
  final int id;
  final String title;
  final String content;
  final String date;
  final bool favorite;

  Entry(this.id, this.title, this.content, this.date, this.favorite);
}

final fakeEntries = [
  Entry(1, 'A quiet morning',
      'Woke up early, made coffee, and just sat by the window for a while.',
      'Aug 16, 2026', true),
  Entry(2, 'Late night thoughts',
      "Couldn't sleep, kept thinking about the app and what to build next.",
      'Aug 16, 2026', false),
  Entry(3, 'Age before beauty',
      'Started reading about system design today. Feels like a whole new mountain to climb, but exciting.',
      'Aug 16, 2026', false),
];

// --- Screen 1: list of entries (like your "list_all_entries") ---
class EntryListScreen extends StatelessWidget {
  const EntryListScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('My Journal')),
      body: ListView.builder(
        padding: const EdgeInsets.all(12),
        itemCount: fakeEntries.length,
        itemBuilder: (context, index) {
          final entry = fakeEntries[index];
          return Card(
            margin: const EdgeInsets.only(bottom: 12),
            child: ListTile(
              title: Text(entry.title,
                  style: const TextStyle(fontWeight: FontWeight.bold)),
              subtitle: Text(
                entry.content,
                maxLines: 2,
                overflow: TextOverflow.ellipsis,
              ),
              trailing: Icon(
                entry.favorite ? Icons.favorite : Icons.favorite_border,
                color: entry.favorite ? Colors.redAccent : Colors.grey,
              ),
              onTap: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (_) => EntryDetailScreen(entry: entry),
                  ),
                );
              },
            ),
          );
        },
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          Navigator.push(
            context,
            MaterialPageRoute(builder: (_) => const AddEntryScreen()),
          );
        },
        child: const Icon(Icons.add),
      ),
    );
  }
}

// --- Screen 2: view one entry (like your "view_entry") ---
class EntryDetailScreen extends StatelessWidget {
  final Entry entry;
  const EntryDetailScreen({super.key, required this.entry});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(entry.title)),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(entry.content, style: const TextStyle(fontSize: 16)),
            const Spacer(),
            Text(entry.date,
                style: TextStyle(color: Colors.grey.shade600)),
          ],
        ),
      ),
    );
  }
}

// --- Screen 3: add entry (like your "add_entry") ---
class AddEntryScreen extends StatelessWidget {
  const AddEntryScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final titleController = TextEditingController();
    final contentController = TextEditingController();

    return Scaffold(
      appBar: AppBar(title: const Text('New Entry')),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          children: [
            TextField(
              controller: titleController,
              decoration: const InputDecoration(labelText: 'Title'),
            ),
            const SizedBox(height: 12),
            TextField(
              controller: contentController,
              maxLines: 8,
              decoration: const InputDecoration(
                labelText: 'What\'s on your mind?',
                alignLabelWithHint: true,
              ),
            ),
            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: () => Navigator.pop(context),
              child: const Text('Save Entry'),
            ),
          ],
        ),
      ),
    );
  }
}