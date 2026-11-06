import React from 'react';
import {LayoutDashboard,FilePlus2,Activity,SlidersHorizontal,Lightbulb,Users,Brain,Info,ShieldCheck} from 'lucide-react';

const items=[
  ['Dashboard','Dashboard',LayoutDashboard],
  ['New Assessment','New Assessment',FilePlus2],
  ['Risk Analysis','Risk Analysis',Activity],
  ['What-if Simulator','What-if Simulator',SlidersHorizontal],
  ['Recommendations','Recommendations',Lightbulb],
  ['Risk Monitoring','Risk Monitoring',Activity],
  ['Applicants','Applicants',Users],
  ['Model Insights','Model Insights',Brain],
  ['About CreditLens','About CreditLens',Info]
];

export default function Sidebar({page,setPage}){
  return (
    <aside className="sidebar">
      <div className="brand">
        <div className="brand-mark"><ShieldCheck size={21} strokeWidth={2.2}/></div>
        <div>
          <b>CreditLens</b>
          <small>Adaptive Risk Intelligence</small>
        </div>
      </div>

      <nav>
        {items.map(([label,key,Icon]) => (
          <button
            key={key}
            className={page===key?'nav-item active':'nav-item'}
            onClick={()=>setPage(key)}
          >
            <Icon size={17}/>
            <span>{label}</span>
          </button>
        ))}
      </nav>
      <div className="sidebar-note">
        <div className="sidebar-note-icon"><ShieldCheck size={16}/></div>
        <b>Built for clearer decisions</b>
        <p>Explore risk signals, compare scenarios, and keep a human in the loop.</p>
        <div className="sidebar-version"><span className="version-dot"/> Prototype workspace <span>v1.0</span></div>
      </div>
    </aside>
  );
}