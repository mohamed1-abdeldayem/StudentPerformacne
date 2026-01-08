import streamlit as st

def sidebar():
    st.markdown("""
      <div class="sidebar border-end shadow-sm">
        <div class="sidebar-header border-bottom">
        <div class="sidebar-brand">Students</div>
      </div>
      <ul class="sidebar-nav">
        <li class="nav-item">
          <a class="nav-link active" href="#">
          <i class="nav-icon cil-speedometer"></i> Dashboard
          </a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">
            <i class="nav-icon cil-speedometer"></i> Statistics
          </a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">
          <i class="nav-icon cil-speedometer"></i> Settings
          </a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">
          <i class="nav-icon cil-speedometer"></i> Logout
          </a>
        </li>
      </ul>
      </div>
    """, unsafe_allow_html=True)
