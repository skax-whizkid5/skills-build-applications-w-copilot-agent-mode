import { NavLink, Navigate, Route, Routes } from 'react-router-dom';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';
import './App.css';

const resolveApiBaseUrl = () => {
  const codespaceName = process.env.REACT_APP_CODESPACE_NAME;
  if (codespaceName && codespaceName.trim()) {
    return `https://${codespaceName.trim()}-8000.app.github.dev`;
  }

  const configured = process.env.REACT_APP_API_BASE_URL;
  if (configured && configured.trim()) {
    return configured.replace(/\/$/, '');
  }

  const hostname = window.location.hostname;
  if (hostname === 'localhost' || hostname === '127.0.0.1') {
    return 'http://localhost:8000';
  }

  if (hostname.endsWith('.app.github.dev')) {
    const backendHost = hostname.replace(/-\d+\.app\.github\.dev$/, '-8000.app.github.dev');
    return `https://${backendHost}`;
  }

  return `${window.location.protocol}//${hostname}:8000`;
};

const apiBaseUrl = resolveApiBaseUrl();
const apiRootUrl = `${apiBaseUrl}/api/`;
const appLogoUrl = `${process.env.PUBLIC_URL}/octofitapp-small.png`;

const navItems = [
  { path: '/users', label: 'Users', Component: Users },
  { path: '/teams', label: 'Teams', Component: Teams },
  { path: '/activities', label: 'Activities', Component: Activities },
  { path: '/leaderboard', label: 'Leaderboard', Component: Leaderboard },
  { path: '/workouts', label: 'Workouts', Component: Workouts },
];

function App() {
  return (
    <div className="app-shell">
      <header className="app-header border-bottom">
        <div className="card border-0 shadow-sm">
          <div className="card-body d-flex flex-column flex-lg-row justify-content-between align-items-lg-center gap-2">
            <div className="d-flex align-items-center gap-3">
              <img src={appLogoUrl} alt="OctoFit logo" className="app-logo" />
              <div>
                <h1 className="h4 mb-1 app-title">OctoFit Tracker</h1>
                <p className="mb-1 small app-subtitle">Backend API: {apiBaseUrl}</p>
              </div>
            </div>
            <div className="text-lg-end">
              <a
                className="app-link link-offset-2 link-underline-opacity-25 link-underline-opacity-100-hover"
                href={apiRootUrl}
                target="_blank"
                rel="noreferrer"
              >
                Open REST API root
              </a>
              <div className="mt-2">
                <a className="btn btn-outline-primary app-btn" href={apiRootUrl} target="_blank" rel="noreferrer">
                  API Root
                </a>
              </div>
            </div>
          </div>
        </div>
      </header>

      <nav className="app-nav nav nav-pills gap-2 px-3 px-md-4 pt-3" aria-label="Main navigation">
        {navItems.map(({ path, label }) => (
          <NavLink
            key={path}
            className={({ isActive }) => `nav-link ${isActive ? 'active' : ''}`}
            to={path}
          >
            {label}
          </NavLink>
        ))}
      </nav>

      <main className="container-fluid px-3 px-md-4 py-3">
        <Routes>
          <Route path="/" element={<Navigate to="/users" replace />} />
          {navItems.map(({ path, Component }) => (
            <Route key={path} path={path} element={<Component apiBaseUrl={apiBaseUrl} />} />
          ))}
          <Route path="*" element={<Navigate to="/users" replace />} />
        </Routes>
      </main>
    </div>
  );
}

export default App;
