'use client'

import React, { useState } from 'react'
import { Terminal, Github, Send, Zap } from 'lucide-react'

export default function CodeiQ() {
  const [activeTab, setActiveTab] = useState('chat')
  const [chatMessages, setChatMessages] = useState([])
  const [message, setMessage] = useState('')
  const [repoUrl, setRepoUrl] = useState('')
  const [repoQuestion, setRepoQuestion] = useState('')
  const [repoAnswer, setRepoAnswer] = useState('')

  const handleSendMessage = () => {
    if (message.trim()) {
      setChatMessages([...chatMessages, { type: 'user', content: message }])
      // Here you would typically call your backend API
      // For demo purposes, we'll just echo the message
      setTimeout(() => {
        setChatMessages(prev => [...prev, { type: 'bot', content: `You said: ${message}` }])
      }, 1000)
      setMessage('')
    }
  }

  const handleRepoAnalysis = () => {
    if (repoUrl && repoQuestion) {
      // Here you would typically call your backend API
      // For demo purposes, we'll just set a mock answer
      setRepoAnswer(`Analysis for ${repoUrl}:\n\nQ: ${repoQuestion}\n\nA: This is a mock answer. In a real implementation, this would be the response from your Gemini API based on the repository analysis.`)
    }
  }

  return (
    <div className="min-h-screen bg-gray-900 text-white font-mono">
      <header className="bg-gray-800 p-4 border-b border-purple-500">
        <div className="container mx-auto flex items-center justify-between">
          <h1 className="text-3xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-purple-400 to-blue-500">
            CodeiQ <Zap className="inline-block ml-2 text-yellow-400" />
          </h1>
          <nav>
            <button
              onClick={() => setActiveTab('chat')}
              className={`mr-4 ${activeTab === 'chat' ? 'text-purple-400' : 'text-gray-400'} hover:text-purple-300 transition-colors`}
            >
              Chat
            </button>
            <button
              onClick={() => setActiveTab('repo')}
              className={`${activeTab === 'repo' ? 'text-blue-400' : 'text-gray-400'} hover:text-blue-300 transition-colors`}
            >
              Repo Analysis
            </button>
          </nav>
        </div>
      </header>

      <main className="container mx-auto mt-8 p-4">
        {activeTab === 'chat' ? (
          <div className="bg-gray-800 rounded-lg shadow-lg p-6 border border-purple-500">
            <h2 className="text-2xl mb-4 text-purple-400">Chat with CodeiQ</h2>
            <div className="h-96 overflow-y-auto mb-4 p-4 bg-gray-900 rounded-md border border-purple-700">
              {chatMessages.map((msg, index) => (
                <div key={index} className={`mb-2 ${msg.type === 'user' ? 'text-right' : 'text-left'}`}>
                  <span className={`inline-block p-2 rounded-lg ${msg.type === 'user' ? 'bg-purple-600' : 'bg-blue-600'}`}>
                    {msg.content}
                  </span>
                </div>
              ))}
            </div>
            <div className="flex">
              <input
                type="text"
                value={message}
                onChange={(e) => setMessage(e.target.value)}
                placeholder="Ask CodeiQ something..."
                className="flex-grow mr-2 p-2 bg-gray-700 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500"
              />
              <button
                onClick={handleSendMessage}
                className="p-2 bg-purple-600 rounded-md hover:bg-purple-700 transition-colors"
              >
                <Send className="h-6 w-6" />
              </button>
            </div>
          </div>
        ) : (
          <div className="bg-gray-800 rounded-lg shadow-lg p-6 border border-blue-500">
            <h2 className="text-2xl mb-4 text-blue-400">GitHub Repository Analysis</h2>
            <input
              type="text"
              value={repoUrl}
              onChange={(e) => setRepoUrl(e.target.value)}
              placeholder="Enter a GitHub repository URL"
              className="w-full mb-4 p-2 bg-gray-700 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
            />
            <textarea
              value={repoQuestion}
              onChange={(e) => setRepoQuestion(e.target.value)}
              placeholder="Ask a question related to the repository"
              className="w-full h-24 mb-4 p-2 bg-gray-700 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 resize-none"
            ></textarea>
            <button
              onClick={handleRepoAnalysis}
              className="w-full p-2 bg-blue-600 rounded-md hover:bg-blue-700 transition-colors mb-4"
            >
              Analyze Repository
            </button>
            <div className="bg-gray-900 rounded-md p-4 h-48 overflow-y-auto border border-blue-700">
              <pre className="whitespace-pre-wrap">{repoAnswer}</pre>
            </div>
          </div>
        )}
      </main>

      <footer className="mt-8 bg-gray-800 p-4 border-t border-purple-500">
        <div className="container mx-auto text-center text-gray-400">
          <p>&copy; 2024 CodeiQ. All rights reserved.</p>
          <p className="mt-2">
            Powered by <Terminal className="inline-block mr-1" /> AI and <Github className="inline-block mx-1" /> GitHub
          </p>
        </div>
      </footer>
    </div>
  )
}

