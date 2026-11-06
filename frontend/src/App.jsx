import React, { useState } from 'react';
import Sidebar from './components/Sidebar';
import Dashboard from './pages/Dashboard';
import Assessment, { RiskAnalysis } from './pages/Assessment';
import Simulator from './pages/Simulator';
import Applicants from './pages/Applicants';
import ModelInsights from './pages/ModelInsights';
import Monitoring from './pages/Monitoring';
import AuthScreen from './components/AuthScreen';
import { LogOut } from 'lucide-react';
import './styles.css';

function SimplePage({ title, text }) {
  return <div className="empty"><h2>{title}</h2><p>{text}</p></div>;
}

export default function App() {
  const [user, setUser] = useState(() => {
    try { return JSON.parse(localStorage.getItem('creditlens_demo_session') || 'null'); }
    catch { return null; }
  });
  const [page, setPage] = useState('Dashboard');
  const [result, setResult] = useState(null);

  function login(profile) {
    localStorage.setItem('creditlens_demo_session', JSON.stringify(profile));
    setUser(profile);
  }
  function logout() {
    localStorage.removeItem('creditlens_demo_session');
    setUser(null); setPage('Dashboard'); setResult(null);
  }

  if (!user) return <AuthScreen onLogin={login} />;

  const content = {
    Dashboard: <Dashboard />,
    'New Assessment': <Assessment setResult={setResult} setPage={setPage} initialProfile={result?.profile} />,
    'Risk Analysis': <RiskAnalysis result={result} />,
    'What-if Simulator': <Simulator result={result} />,
    Recommendations: <RiskAnalysis result={result} />,
    'Risk Monitoring': <Monitoring selectedId={result?.applicant_id} />,
    Applicants: <Applicants setResult={setResult} setPage={setPage} />,
    'Model Insights': <ModelInsights />,
    'About CreditLens': <SimplePage title="About CreditLens" text="CreditLens is an academic machine-learning decision-support prototype. It combines risk prediction, multi-dimensional scoring, explainability, what-if simulation, recommendations, and monitoring in one workflow. Predictions should not be used as the sole basis for real-world lending decisions." />
  };
  const initials = (user.name || user.email || 'CL').split(/[\s@._-]+/).filter(Boolean).slice(0, 2).map(s => s[0].toUpperCase()).join('');

  return <div className="app-shell">
    <Sidebar page={page} setPage={setPage} />
    <main>
      <header>
        <div className="header-title"><span className="eyebrow">CREDIT RISK INTELLIGENCE / WORKSPACE</span><h1>{page}</h1></div>
        <div className="header-meta"><div className="status"><i/> Workspace ready</div><span className="header-divider"/><div className="profile-chip"><span className="profile-avatar">{initials}</span><div><b>{user.name || 'CreditLens user'}</b><small>{user.email}</small></div></div><button className="logout-button" onClick={logout} title="Sign out"><LogOut size={16}/><span>Sign out</span></button></div>
      </header>
      <section className="content">{content[page]}</section>
      <footer className="app-footer"><span>CreditLens <span className="footer-dot">·</span> Risk intelligence workspace</span><span>Academic prototype · Human review required</span></footer>
    </main>
  </div>;
}
