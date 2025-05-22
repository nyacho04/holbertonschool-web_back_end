const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');
    const lines = data.split('\n').filter(line => line.trim() !== '');
    if (lines.length === 0) {
      throw new Error('Cannot load the database');
    }

    const students = lines.slice(1).filter(line => line.trim() !== '');
    const fields = {};
    students.forEach((line) => {
      const parts = line.split(',');
      if (parts.length < 4) return;
      const firstname = parts[0].trim();
      const field = parts[3].trim();
      if (!fields[field]) {
        fields[field] = [];
      }
      fields[field].push(firstname);
    });

    console.log(`Number of students: ${students.length}`);
    for (const [field, names] of Object.entries(fields)) {
      console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
    }
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
