import React, { useState } from 'react';
import { ShieldCheck, Eye, EyeOff, ArrowRight, Sparkles, LockKeyhole, Activity, CircleCheck, Fingerprint } from 'lucide-react';

const DEMO_EMAIL = 'demo@creditlens.app';
const DEMO_PASSWORD = 'CreditLens123!';

export default function AuthScreen({ onLogin }) {
  const [mode, setMode] = useState('login');
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [showPassword, setShowPassword] = useState(false);
  const [error, setError] = useState('');
  const [notice, setNotice] = useState('');

  function submit(e) {
    e.preventDefault(); setError(''); setNotice('');
    const cleanEmail = email.trim().toLowerCase();
    if (!cleanEmail || !password) { setError('Enter your email and password to continue.'); return; }
    if (mode === 'signup') {
      if (!name.trim()) { setError('Please enter your name.'); return; }
      if (password.length < 8) { setError('Use at least 8 characters for this demo password.'); return; }
      const users = JSON.parse(localStorage.getItem('creditlens_demo_users') || '{}');
      if (users[cleanEmail]) { setError('An account with this email already exists. Try signing in.'); return; }
      users[cleanEmail] = { name: name.trim(), password };
      localStorage.setItem('creditlens_demo_users', JSON.stringify(users));
      onLogin({ name: name.trim(), email: cleanEmail });
      return;
    }
    if (cleanEmail === DEMO_EMAIL && password === DEMO_PASSWORD) {
      onLogin({ name: 'Demo Analyst', email: DEMO_EMAIL }); return;
    }
    const users = JSON.parse(localStorage.getItem('creditlens_demo_users') || '{}');
    if (users[cleanEmail] && users[cleanEmail].password === password) {
      onLogin({ name: users[cleanEmail].name, email: cleanEmail }); return;
    }
    setError('Those details did not match a demo account. Try the demo login below.');
  }

  function useDemo() { setEmail(DEMO_EMAIL); setPassword(DEMO_PASSWORD); setMode('login'); setError(''); setNotice('Demo credentials filled in. Click Sign in to enter the workspace.'); }

  return <div className="auth-page">
    <section className="auth-story">
      <div className="auth-brand"><span className="auth-logo"><ShieldCheck size={23}/></span><span>CreditLens<small>ADAPTIVE RISK INTELLIGENCE</small></span></div>
      <div className="story-copy">
        <div className="story-kicker"><Sparkles size={14}/> CLARITY BEHIND EVERY SCORE</div>
        <h1>See the story<br/>behind <em>credit risk.</em></h1>
        <p>A clearer workspace for exploring credit profiles, understanding risk signals, and testing better scenarios.</p>
        <div className="story-features">
          <div><span><Activity size={17}/></span><div><b>Risk, made readable</b><small>Explore scores and contributing signals.</small></div></div>
          <div><span><Fingerprint size={17}/></span><div><b>Explainable by design</b><small>Understand the factors behind predictions.</small></div></div>
          <div><span><CircleCheck size={17}/></span><div><b>Compare what-if scenarios</b><small>See how profile changes may affect outcomes.</small></div></div>
        </div>
      </div>
      <div className="story-bottom"><span>BUILT FOR THOUGHTFUL DECISIONS</span><span>ACADEMIC DEMO · 2026</span></div>
      <div className="auth-orbit orbit-one"/><div className="auth-orbit orbit-two"/><div className="auth-orbit orbit-three"/>
    </section>
    <section className="auth-side">
      <div className="auth-card-wrap">
        <div className="mobile-auth-brand"><span className="auth-logo"><ShieldCheck size={22}/></span><b>CreditLens</b></div>
        <div className="auth-heading"><span className="auth-mini-label">YOUR WORKSPACE AWAITS</span><h2>{mode === 'login' ? 'Welcome back' : 'Create your account'}</h2><p>{mode === 'login' ? 'Sign in to continue to your risk intelligence workspace.' : 'Set up a demo profile to explore CreditLens.'}</p></div>
        <div className="auth-tabs"><button className={mode === 'login' ? 'selected' : ''} onClick={() => {setMode('login');setError('');setNotice('');}}>Sign in</button><button className={mode === 'signup' ? 'selected' : ''} onClick={() => {setMode('signup');setError('');setNotice('');}}>Create account</button></div>
        <form className="auth-form" onSubmit={submit}>
          {mode === 'signup' && <label>Full name<input value={name} onChange={e=>setName(e.target.value)} placeholder="e.g. Alex Morgan" autoComplete="name"/></label>}
          <label>Email address<input type="email" value={email} onChange={e=>setEmail(e.target.value)} placeholder="you@example.com" autoComplete="email"/></label>
          <label>Password<span className="password-wrap"><input type={showPassword?'text':'password'} value={password} onChange={e=>setPassword(e.target.value)} placeholder={mode==='signup'?'At least 8 characters':'Enter your password'} autoComplete={mode==='login'?'current-password':'new-password'}/><button type="button" className="show-password" aria-label={showPassword?'Hide password':'Show password'} onClick={()=>setShowPassword(!showPassword)}>{showPassword?<EyeOff size={17}/>:<Eye size={17}/>}</button></span></label>
          {error && <div className="auth-message error">{error}</div>}{notice && <div className="auth-message info">{notice}</div>}
          <button className="auth-submit" type="submit">{mode==='login'?'Sign in to CreditLens':'Create demo account'}<ArrowRight size={17}/></button>
        </form>
        {mode==='login' && <><div className="auth-separator"><span>OR TRY THE PROJECT</span></div><button className="demo-button" onClick={useDemo}><span className="demo-icon"><Sparkles size={17}/></span><span><b>Use demo account</b><small>Instant access · no setup needed</small></span><ArrowRight size={16}/></button></>}
        <div className="auth-security"><LockKeyhole size={14}/><span>Demo authentication runs in this browser only. Do not use a real password.</span></div>
        <div className="auth-legal">CreditLens is an academic decision-support prototype. Predictions are not lending advice.</div>
      </div>
    </section>
  </div>;
}
