'use client'; // Tells Next.js this runs in the browser

import { useEffect, useState } from 'react';

export default function StudentsPage() {
  const [students, setStudents] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Request the backend API (run FastAPI on port 8000)
    fetch('http://127.0.0.1:8000/api/students')
      .then((res) => {
        if (!res.ok) throw new Error('Could not pull the student roster data.');
        return res.json();
      })
      .then((data) => {
        setStudents(data);
        setLoading(false);
      })
      .catch((err) => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  if (loading) return <div className="p-10 text-xl font-sans text-gray-600">Loading student roster...</div>;
  if (error) return <div className="p-10 text-xl font-sans text-red-500">Error: {error}</div>;

  return (
    <div className="p-10 font-sans max-w-5xl mx-auto">
      <h1 className="text-3xl font-bold text-gray-800 border-b-2 border-gray-100 pb-4 mb-6">
        School Management System - Student Roster
      </h1>

      {students.length === 0 ? (
        <p className="text-gray-500 text-lg">No students found. Add some rows inside your backend /docs panel!</p>
      ) : (
        <div className="overflow-x-auto shadow-md rounded-lg border border-gray-200">
          <table className="w-full text-left border-collapse bg-white">
            <thead>
              <tr className="bg-gray-50 text-gray-700 font-semibold uppercase text-sm border-b border-gray-200">
                <th className="p-4">Reg No</th>
                <th className="p-4">Full Name</th>
                <th className="p-4">Email</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-100 text-gray-600 text-md">
              {students.map((student) => (
                <tr key={student.id} className="hover:bg-gray-50 transition-colors">
                  <td className="p-4 font-bold text-blue-600">{student.reg_no}</td>
                  <td className="p-4">{student.first_name} {student.middle_name || ''} {student.surname}</td>
                  <td className="p-4">{student.email}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}